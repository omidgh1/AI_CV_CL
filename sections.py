import json
import streamlit as st

class AppSection:
    def __init__(self) -> None:
        pass

    def userinfo(self):
        st.header('Enter the following information')
        col1, col2 = st.columns(2)
        user_name = col1.text_input('Enter your Name')
        company_name = col2.text_input('Enter the company Name')
        user_phone = col1.text_input('Enter your Phone Number')
        user_address = col2.text_input('Enter your Address')
        email_address = col1.text_input('Enter your Email Address')
        return user_name, company_name, user_phone, user_address, email_address

    def uploadfile(self) -> str:
        st.header('Upload your Resume')
        uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
        return uploaded_file

    def colorpicker(self) -> str:
        """
        Displays the color picker section.
        """
        st.header('Choose a Color Scheme')
        color_code = st.color_picker("Choose a Color", "#000000")
        st.write('The current color is', color_code)
        return color_code

    def description(self) -> str:
        st.header('Add a Job Description')
        job_description = st.text_area('Enter the job description here', height=300)
        return job_description

    def resume_edit(self,result_data, phone, user_address):
        data = json.loads(result_data)

        user_information = data.get('user_information')

        st.title("Edit Generated Resume")
        st.subheader("Information")

        profile_description = st.text_area('Profile Description', user_information.get('profile_description'),
                                           height=150)
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input('Name', user_information.get('name'))
            email = st.text_input('Email', user_information.get('email'))
            github = st.text_input('Github', user_information.get('github'))
            address = st.text_input('Home Address', user_address)

        with col2:
            main_job_title = st.text_input('Main job title', user_information.get('main_job_title'))
            linkedin = st.text_input('Linkedin', user_information.get('linkedin'))
            phone = st.text_input('phone', phone)

        data['user_information']['name'] = name
        data['user_information']['email'] = email
        data['user_information']['phone'] = phone
        data['user_information']['github'] = github
        data['user_information']['address'] = address
        data['user_information']['main_job_title'] = main_job_title
        data['user_information']['linkedin'] = linkedin
        data['user_information']['profile_description'] = profile_description

        info = {'name': name, 'email': email, 'phone': phone, 'github': github, 'address': address,
                'main_job_title': main_job_title, 'linkedin': linkedin}

        col3, col4 = st.columns(2)
        job_experiences = user_information.get('experiences')
        for i in range(len(job_experiences)):
            col3.subheader(f'Company {i+1} Information')
            col4.subheader("    ")
            globals()[f'job_title_{i}'] = col3.text_input(f"Job Title {i+1}",job_experiences[i].get('job_title'))
            globals()[f'company_{i}'] = col4.text_input(f"Company {i+1}",job_experiences[i].get('company'))
            globals()[f'start_date_{i}'] = col3.text_input(f"Start Date {i + 1}", job_experiences[i].get('start_date'))
            globals()[f'end_date_{i}'] = col4.text_input(f"End Date {i + 1}", job_experiences[i].get('end_date'))
            st.subheader(f'{job_experiences[i].get("company")} Tasks')
            globals()[f'tasks_{i}'] = st.text_area(f"Company Tasks {i + 1}", "===".join(job_experiences[i].get('four_tasks')),height=150)

            data['user_information']['experiences'][i]['job_title'] = globals()[f'job_title_{i}']
            data['user_information']['experiences'][i]['company'] = globals()[f'company_{i}']
            data['user_information']['experiences'][i]['start_date'] = globals()[f'start_date_{i}']
            data['user_information']['experiences'][i]['end_date'] = globals()[f'end_date_{i}']
            data['user_information']['experiences'][i]['four_tasks'] = globals()[f'tasks_{i}'].split("===")

        col5, col6 = st.columns(2)
        education = user_information.get('education')
        for i in range(len(education)):
            col5.subheader(f'institution {i + 1} Information')
            col6.subheader("    ")
            globals()[f'institution_{i}'] = col5.text_input(f"Institution {i + 1}", education[i].get('institution'))
            globals()[f'degree_{i}'] = col6.text_input(f"Degree {i + 1}", education[i].get('degree'))
            globals()[f'education_start_date_{i}'] = col5.text_input(f"Education Start Date {i + 1}", education[i].get('start_date'))
            globals()[f'education_end_date_{i}'] = col6.text_input(f"Education End Date {i + 1}", education[i].get('end_date'))
            st.subheader(f'{education[i].get("institution")} Description')
            globals()[f'education_description_{i}'] = st.text_area(f"Education Description {i + 1}",education[i].get('description'),height=150)

            data['user_information']['education'][i]['institution'] = globals()[f'institution_{i}']
            data['user_information']['education'][i]['degree'] = globals()[f'degree_{i}']
            data['user_information']['education'][i]['start_date'] = globals()[f'education_start_date_{i}']
            data['user_information']['education'][i]['end_date'] = globals()[f'education_end_date_{i}']
            data['user_information']['education'][i]['description'] = globals()[f'education_description_{i}']

        skills = data['user_information']['skills']
        st.subheader("Skills")
        hard_skills = st.text_area("Hard Skills"," , ".join(skills.get('hard_skills')),height=150)
        soft_skills = st.text_area("Soft Skills", " , ".join(skills.get('soft_skills')), height=150)
        data['user_information']['skills']['hard_skills'] = hard_skills.split(",")
        data['user_information']['skills']['soft_skills'] = soft_skills.split(",")

        col7, col8 = st.columns(2)
        projects = data['projects']
        st.subheader("Projects")
        for i in range(len(projects)):
            globals()[f'project_name_{i}'] = st.text_input(f"Project name {i + 1}", projects[i].get('project_name'))
            globals()[f'project_description_{i}'] = st.text_area(f"Project Description {i + 1}", projects[i].get('project_description'),height=100)

            data['projects'][i]['project_name'] = globals()[f'project_name_{i}']
            data['projects'][i]['project_description'] = globals()[f'project_description_{i}']

        col9, col10 = st.columns(2)
        certificates = data['certificate']
        st.subheader("Certificates")
        for i in range(len(certificates)):
            col9.subheader(f'Certificates {i + 1} Information')
            col10.subheader("  ")
            globals()[f'certificate_name_{i}'] = col9.text_input(f"Certificate Name {i + 1}", certificates[i].get('name'))
            globals()[f'certificate_institution_{i}'] = col10.text_input(f"Certificate Institution {i + 1}", certificates[i].get('institution'))
            globals()[f'certificate_description_{i}'] = st.text_area(f"Certificate Description {i + 1}", certificates[i].get('description'),height=150)

            data['certificate'][i]['name'] = globals()[f'certificate_name_{i}']
            data['certificate'][i]['institution'] = globals()[f'certificate_institution_{i}']
            data['certificate'][i]['description'] = globals()[f'certificate_description_{i}']

        return data, info

    def cl_edit(self, result_data,social_info):
        data = json.loads(result_data)
        greeting = data['Salutation_or_greeting']
        opening = data['opening_paragraph']
        middle = data['middle_paragraph']
        closing = data['closing_paragraph']

        st.title("Edit Generated Cover Letter")

        st.subheader("Information")
        col3,col4 = st.columns(2)
        user_name_family = col3.text_input('CoverLetter Name', social_info['name'])
        phone_num = col4.text_input('CoverLetter Phone', social_info['phone'])
        email_add = col3.text_input('CoverLetter EmailAddress',social_info['email'])
        job_title = col4.text_input('CoverLetter Main job Title',social_info['main_job_title'])
        address = col3.text_input('CoverLetter Address', social_info['address'])
        linkedin = col4.text_input('CoverLetter Linkedin',social_info['linkedin'])
        github = col3.text_input('CoverLetter Github', social_info['github'])


        st.subheader("Salutation or greeting")
        greeting_edit = st.text_input('Salutation or greeting', greeting)

        st.subheader("Opening paragraph")
        opening_edit = st.text_area('Opening paragraph', opening, height=150)
        st.subheader("Middle paragraph")
        middle_edit = st.text_area('Middle paragraph', middle, height=150)
        st.subheader("Closing paragraph")
        closing_edit = st.text_area('Closing paragraph', closing, height=150)

        data['email'] = email_add
        data['address'] = address
        data['name'] = user_name_family
        data['phone'] = phone_num
        data['github'] = github
        data['linkedin'] = linkedin
        data['job_title'] = job_title
        data['salutation_or_greeting'] = greeting_edit
        data['opening_paragraph'] = opening_edit
        data['middle_paragraph'] = middle_edit
        data['closing_paragraph'] = closing_edit


        return data


