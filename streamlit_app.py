import os, streamlit as st
import json
from sections import AppSection
from ats import similarity_score
from tools import ToolKit
from dotenv import load_dotenv
from AI_generator import ResumeGenerator, CoverGenerator
from pdf_creation import create_resume, create_cover_letter, create_pdf


def info_required(app, tool):
    user_name, company_name, user_phone, user_address, email_address = app.userinfo()
    st.session_state.user_info = {"user_name": user_name, "company_name": company_name,
                                  "user_phone": user_phone, "user_address": user_address,
                                  "email_address": email_address}
    job_description = app.description()
    st.session_state.job_description = job_description
    uploaded_file = app.uploadfile()
    if uploaded_file is not None:
        cv_text = tool.pdf_to_text(uploaded_file)
        st.session_state.resume_content = cv_text
        st.success('File Uploaded Successfully')

def ats_check():
    if 'job_description' in st.session_state:
        if "edited_resume_content" not in st.session_state:
            cv_text_before = st.session_state.resume_content
            similarity, missing_keywords = similarity_score(job_description=st.session_state.job_description,
                                                            cv_text=cv_text_before)
            st.sidebar.write(f"Similarity Score of main CV: {similarity:.2f}%")
            st.sidebar.write(f"missing keywords: {missing_keywords}")
        else:
            cv_text_before = st.session_state.resume_content
            cv_text_after = st.session_state.edited_resume_content
            similarity_before,missing_keywords = similarity_score(job_description=st.session_state.job_description,
                                                            cv_text=cv_text_before)
            similarity_after, missing_keywords = similarity_score(job_description=st.session_state.job_description,
                                                            cv_text=cv_text_after)
            st.sidebar.write(f"Similarity Score of main CV: {similarity_before:.2f}%")
            st.sidebar.write(f"Similarity Score of generated CV: {similarity_after:.2f}%")
            st.sidebar.write(f"missing keywords: {missing_keywords}")

def keyword_extraction_ai(API_KEY,tool,job_description):
    keyword_gen = ResumeGenerator(API_KEY=API_KEY, model_name="mixtral-8x22b-instruct")
    prompt_keyword = tool.create_prompt("prompts/keywords.txt")
    keywords = keyword_gen.extract_keywords_ai(prompt_keyword, job_description)
    st.session_state.keywords_ai = keywords
    return keywords

def resume_generator(API_KEY, tool, cv_text, job_description, keywords):
    cv_gen = ResumeGenerator(API_KEY=API_KEY, model_name="mixtral-8x22b-instruct")
    prompt = tool.create_prompt("prompts/test.txt")
    result = cv_gen.generate_resume(prompt, cv_text, 'Balanced', 'English', keywords, job_description)
    # Display the JSON result in a text area
    result_dict = json.loads(result)
    formatted_json = json.dumps(result_dict, indent=4)
    return formatted_json


def cl_generator(API_KEY, tool, job_description, company_name, resume_file, keywords):
    if os.path.exists(resume_file):
        with open(resume_file, "rb") as f:
            pdf_data = f.read()
        with open(resume_file, "rb") as f:
            pdf_text = tool.pdf_to_text(f)
    else:
        pdf_text = st.session_state.resume_content
    cl_gen = CoverGenerator(API_KEY=API_KEY, model_name="mixtral-8x22b-instruct")
    prompt = tool.create_prompt("prompts/coverletter.txt")
    result = cl_gen.generate_coverletter(prompt, pdf_text, company_name, 'Balanced', 'English', keywords,
                                         job_description)
    result_dict = json.loads(result)
    formatted_json = json.dumps(result_dict, indent=4)
    return formatted_json


def resume_edit(app, tool, file_format, color_code, phone, user_address):
    edited_data, social_info = app.resume_edit(st.session_state.generated_resume_data, phone, user_address)
    st.session_state.social_info = social_info
    edited_html = create_resume(data=edited_data)

    compile_resume = st.button('***Compile Resume***')
    if compile_resume:
        pdf_format = create_pdf(data_html=edited_html, filename=file_format, color_code=color_code)
        if pdf_format:
            with open(file_format, "rb") as f:
                pdf_data = f.read()
            with open(file_format, "rb") as f:
                pdf_text = tool.pdf_to_text(f)

            st.session_state.edited_resume_content = pdf_text
            st.download_button("Download Generated Resume", pdf_data, file_format, False)

def coverletter_edit(app, tool, file_format, color_code):
    edited_data = app.cl_edit(st.session_state.generated_coverletter_data,st.session_state.social_info)
    edited_html = create_cover_letter(edited_data)

    compile_cl = st.button('***Compile cl***')
    if compile_cl:
        pdf = create_pdf(data_html=edited_html, filename=file_format, color_code=color_code)
        with open(file_format, "rb") as f:
            pdf_data = f.read()
        with open(file_format, "rb") as f:
            pdf_text = tool.pdf_to_text(f)
        st.download_button("Download Generated CoverLetter", pdf_data, file_format, False)

def remove_generated_file():
    for filename in os.listdir("."):
        if filename.endswith('.pdf'):
            os.remove(filename)

def main():
    app = AppSection()
    tool = ToolKit()
    load_dotenv()
    API_KEY = os.getenv("OCTO_AI_TOKEN")
    info_required(app, tool)
    color_code = app.colorpicker()
    job_description = st.session_state.job_description
    user_name = st.session_state.user_info["user_name"]
    phone = st.session_state.user_info['user_phone']
    email = st.session_state.user_info['email_address']
    user_address = st.session_state.user_info['user_address']
    resume_name = f"{user_name.replace(' ', '_').lower()}_resume.pdf"
    coverletter_name = f"{user_name.replace(' ', '_').lower()}_coverletter.pdf"
    resume_generation = st.sidebar.button('Generate Resume')
    coverletter_generation = st.sidebar.button('Generate CoverLetter')
    ats_generation = st.sidebar.button('Similarity Checking')
    remove_files = st.sidebar.button('Remove Files')
    if remove_files:
        remove_generated_file()

    st.sidebar.header("Similarity Score")
    if ats_generation:
        with st.spinner('ATS Checking...'):
            ats_check()

    if resume_generation:
        with st.spinner('Generating Resume...'):
            if "keywords_ai" not in st.session_state:
                keywords = keyword_extraction_ai(API_KEY, tool, job_description)
            else:
                keywords = st.session_state.keywords_ai
            ai_cv_result = resume_generator(API_KEY, tool, cv_text=st.session_state.resume_content,
                                         job_description=job_description,keywords=keywords)
        st.session_state.generated_resume_data = ai_cv_result
    if 'generated_resume_data' in st.session_state:
        resume_edit(app, tool, resume_name, color_code, phone, user_address)

    if coverletter_generation:
        with st.spinner('Generating CoverLetter...'):
            if "keywords_ai" not in st.session_state:
                keywords = keyword_extraction_ai(API_KEY, tool, job_description)
            else:
                keywords = st.session_state.keywords_ai
            ai_cl_result = cl_generator(API_KEY, tool, job_description=st.session_state.job_description,
                                     company_name=st.session_state.user_info['company_name'],
                                     resume_file=resume_name,
                                        keywords=keywords)
        st.session_state.generated_coverletter_data = ai_cl_result
    if "generated_coverletter_data" in st.session_state:
        main_job_title = st.session_state.edited_resume_content.split('\n')[1]
        coverletter_edit(app, tool, coverletter_name, color_code)



if __name__ == "__main__":
    main()
