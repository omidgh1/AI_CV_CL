from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import json
from datetime import datetime


#def parse_user_information(data: dict) -> str:
#    user_information = data["user_information"]
#    user_information_html = f"""
#    <header>
#        <h1 style="text-align: center;">{user_information['name']}</h1>
#        <p style="text-align: center;">{user_information['main_job_title']}</p>
#        <p style="text-align: center;">{user_information['address']}</p>
#        <p style="text-align: center;"> {user_information['email']} - {user_information['phone']} -
#        <a href="https://github.com/{user_information["github"]}" target="_blank">&nbsp;{user_information["github"]}</a> -
#        <a href="https://linkedin.com/in/{user_information['linkedin']}" target="_blank">&nbsp;{user_information['linkedin']}</a></p>
#        <h2>SUMMARY</h2>
#        <p style="text-align: justify;">{user_information['profile_description']}</p>
#    </header>
#    """
#    return user_information_html

def parse_user_information(data: dict) -> str:
    user_information = data["user_information"]
    user_information_html = f"""
        <header>
            <div style="display: flex; justify-content: space-between; width:850px;">
              <div style="flex: 1; margin-right: 0px;">
                <h1 style="margin-bottom: 0;">{user_information['name']}</h1>
                <p style="margin-top: 0;">{user_information['main_job_title']}</p>
              </div>
              <div style="flex: 1;">
                <p style="margin: 0;">
                  address: {user_information['address']}<br>
                  email: <a href="mailto:{user_information['email']}">{user_information['email']}</a><br>
                  phone: <a href="tel:{user_information['phone']}">{user_information['phone']}</a><br>
                  github: <a href="https://github.com/{user_information["github"]}" target="_blank">{user_information["github"]}</a><br>
                  linkedin: <a href="https://linkedin.com/in/{user_information['linkedin']}" target="_blank">{user_information['linkedin']}</a>
                </p>
              </div>
            </div>
            <h2>SUMMARY</h2>
            <p style="text-align: justify;margin-top: -10px;">{user_information['profile_description']}</p>
        </header>
        """
    return user_information_html


def parse_experiences(data: dict) -> str:
    experiences = data["user_information"]["experiences"]
    if experiences == []:
        return ""
    experiences_html = "<section><h2>EXPERIENCE</h2>"
    for experience in experiences:
        experience_html = f"""
        <div style="display: flex; justify-content: space-between; margin-top: -20px;">
            <p><strong>{experience['job_title']} - <i>{experience['company']}</i></strong></p>
            <p>{experience['start_date']} to {experience['end_date']}</p>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: -20px;">
        <ul>
        """
        for task in experience["four_tasks"]:
            experience_html += f'<li style="text-align: justify;">{task}</li>'
        experience_html += "</ul>"
        experience_html += "</div>"
        experiences_html += experience_html
    experiences_html += "</section>"
    return experiences_html

def parse_education(data: dict) -> str:
    education = data["user_information"]["education"]
    if education == []:
        return ""
    education_html = "<section><h2>EDUCATION</h2>"
    for institution in education:
        institution_html = f"""
        <div style="display: flex; justify-content: space-between; margin-top: -20px;">
            <p><strong>{institution['degree']} - <i>{institution['institution']}</i></strong></p>
            <p>{institution['start_date']} to {institution['end_date']}</p>
        </div>
        <p style="margin-top: -10px; text-align: justify;">{institution['description']}</p>
        """
        education_html += institution_html
    education_html += "</section>"
    return education_html

def parse_skills(data: dict) -> str:
    skills = data["user_information"]["skills"]
    if skills["hard_skills"] == [] and skills["soft_skills"] == []:
        return ""
    skills_html = f"""
    
    <section>
    <h2>SKILLS</h2>
    <p><strong>Hard Skills</p></strong>
    <div style="display: flex; justify-content: space-between; margin-top: -5x;">
    <p style="text-align: justify;margin-top: -10px;">{", ".join(skills["hard_skills"])}</p>
    </div>
    <div style="display: flex; justify-content: space-between; margin-top: -20px;"></div>
    <p><strong>Soft Skills</p></strong>
    <div style="display: flex; justify-content: space-between; margin-top: -5px;">
    <p style="text-align: justify;margin-top: -10px;">{", ".join(skills["soft_skills"])}</p>
    </div>
    </section>
    """

    return skills_html

def parse_projects(data: dict) -> str:
    projects = data["projects"]
    if projects == []:
        return ""

    projects_html = "<section><h2>PROJECTS</h2>"
    for project in projects:
        project_html = f"""
            <div style="display: flex; justify-content: space-between; margin-top: -20px;">
                <p><strong>{project['project_name']}</strong></p>
            </div>
            <p style="margin-top: -10px; text-align: justify;">{project['project_description']}</p>
            """
        projects_html += project_html
    projects_html += "</section>"

    return projects_html

def parse_hobbies(data: dict) -> str:
    if data["user_information"]["hobbies"] == []:
        return ""
    hobbies = data["user_information"]["hobbies"]
    hobbies_html = "<section><h2>HOBBIES</h2><ul>"
    for hobby in hobbies:
        hobbies_html += f"<li>{hobby}</li>"
    hobbies_html += "</ul></section>"
    return hobbies_html

def parse_certificate(data: dict) -> str:
    certifications = data["certificate"]
    if certifications == []:
        return ""
    certifications_html = "<section><h2>CERTIFICATES</h2>"
    for certification in certifications:
        certification_html = f"""
        <div style="display: flex; justify-content: space-between; margin-bottom: 0;margin-top: -20px;">
            <p><strong>{certification['name']} ({certification['institution']})</strong></p>
            <p>{certification['date']}</p>
        </div>
        <p style="margin-top: -10px; text-align: justify;">{certification['description']}</p>
        """
        certifications_html += certification_html
    certifications_html += "</section>"
    return certifications_html

def parse_extra_curricular_activities(data: dict) -> str:
    extra_curricular_activities = data["extra_curricular_activities"]
    if extra_curricular_activities == []:
        return ""
    extra_curricular_activities_html = "<section><h2>EXTRA-CURRICULAR ACTIVITIES</h2>"
    for activity in extra_curricular_activities:
        activity_html = f"""
        <h3>{activity['name']}</h3>
        <p style="margin-top: 0px; text-align: justify;">{activity['description']}</p>
        """
        extra_curricular_activities_html += activity_html
    extra_curricular_activities_html += "</section>"
    return extra_curricular_activities_html
def create_resume(data) -> str:
    #data = json.loads(data)
    user_information_html = parse_user_information(data)
    experiences_html = parse_experiences(data)
    education_html = parse_education(data)
    skills_html = parse_skills(data)
    projects_html = parse_projects(data)
    hobbies_html = parse_hobbies(data)
    certificates_html = parse_certificate(data)
    try:
        extra_curricular_activities_html = parse_extra_curricular_activities(data)
    except:
        extra_curricular_activities_html = ""
    resume_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="index.css">
    </head>
    <body>
        {user_information_html}
        {skills_html}
        {experiences_html}
        {education_html}
        {certificates_html}
        {projects_html}
    </body>
    </html>
    """
    return resume_html

def perfect_css_style(color_code : str) -> str:
    css = f"""
    body {{
        font-family: 'Times New Roman', Times, serif;
        font-size: 14px;
        line-height: 1.5;
        background-color: #ffffff;
        margin: 0;
        margin-top: -50px;
        padding: 0;
        padding-top: 0px;
    }}

    header, section {{
        padding: 10px 20px;
        margin-top: -10x;
    }}

    header h1 {{
        font-size: 36px;
        color: {color_code};
    }}

    header p, header a, section a {{
        font-size: 14px;
        color: #333333;
        text-decoration: none;
    }}

    h2 {{
        font-size: 9px;
        color: #333333;
        border-bottom: 1px solid #dddddd;
        padding-bottom: 5px;
        margin-top: 10px;
        margin-bottom: 10px;
    }}

    h3 {{
        font-size: 12px;
        color: #333333;
    }}

    ul {{
        padding: 0;
    }}

    ul li {{
        list-style: inside;
        margin-bottom: 2px;
    }}

    a:hover {{
        text-decoration: underline;
    }}

    @media print {{
        body {{
            background-color: #ffffff;
        }}

        header, section {{
            padding: 0;
            border: none;
        }}

        h2 {{
            font-size: 20px;
            color: {color_code};
            border-bottom: 2px solid {color_code};
        }}
    }}
    """
    return css

def create_cover_letter(data) -> str:
    user_information_html = f"""
            <header>
                <div style="display: flex; justify-content: space-between; width:850px;">
                  <div style="flex: 1; margin-right: 0px;">
                    <h1 style="margin-top: 30px;">{data['name']}</h1>
                    <p style="margin-top: -20px;">{data['job_title']}</p>
                    <p style="margin-top: -15px;"> {datetime.now().strftime("%d/%m/%Y")}</p> 
                  </div>
                  <div style="flex: 1;">
                    <p style="margin-top: 30px;">
                      address: {data['address']}<br>
                      email: <a href="mailto:{data['email']}">{data['email']}</a><br>
                      phone: <a href="tel:{data['phone']}">{data['phone']}</a><br>
                      github: <a href="https://github.com/{data["github"]}" target="_blank">{data["github"]}</a><br>
                      linkedin: <a href="https://linkedin.com/in/{data['linkedin']}" target="_blank">{data['linkedin']}</a>
                    </p>
                  </div>
                </div>
            </header>
            """


    #user_information_html = f"""
    #    <header>
    #        <h1 style="text-align: center;">{data['name']}</h1>
    #        <p style="text-align: center;">{data['job_title']}</p>
    #        <p style="text-align: center;"> {data['email']} - {data['phone']}</p>
    #        <p style="text-align: center;">{data['address']}</p>
    #        <p style="text-align: center;"> {datetime.now().strftime("%Y-%m-%d")}</p>
    #    </header>
    #    """
    paragraph_html = f"""
            <p style="text-align: justify;">{data['salutation_or_greeting']},</p>
            <p style="text-align: justify;">{data['opening_paragraph']},</p>
            <p style="text-align: justify;">{data['middle_paragraph']},</p>
            <p style="text-align: justify;">{data['closing_paragraph']},</p>
        """
    ending_html = f"""
            <p style="text-align: justify;">Sincerely,<br />{data['name']}</p>
        """
    cover_letter_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="index.css">
        </head>
        <body>
            {user_information_html}
            {paragraph_html}
            {ending_html}
        </body>
        </html>
        """
    return cover_letter_html

def create_pdf(data_html: str, filename: str, color_code="#000000") -> bool:
    try:
        font_config = FontConfiguration()
        html = HTML(string=f"""{data_html}""")
        css = CSS(string=f'''{perfect_css_style(color_code)}''', font_config=font_config)
        html.write_pdf(filename, stylesheets=[css], font_config=font_config)
        return True
    except Exception as e:
        # print(f"Failed to create PDF: {e}")
        return False