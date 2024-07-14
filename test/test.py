from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

data_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="index.css">
    </head>
    <body>
        
    <header>
        <table style="width: 763px;">
            <tbody>
            <tr>
            <td style="width: 408px;">
            <h1>Omid Ghamiloo</h1>
            <p>AI, Data Science, DevOps, and Cloud Intern</p>
            </td>
            <td style="width: 339px;">address: Piazza dei pini, 14<br />email: omid.ghamiloo@gmail.com<br />phone: +393891249525<br />github: <a href="https://github.com/omid-ghamiloo" target="_blank" rel="noopener">omid-ghamiloo</a><br />linkedin:<a href="https://linkedin.com/in/omidgh1" target="_blank" rel="noopener">omidgh1</a></td>
            </tr>
            </tbody>
            </table>
        <h2>SUMMARY</h2>
        <p style="text-align: justify;">A passionate and dedicated AI, Data Science, DevOps, and Cloud Intern with a strong foundation in Python, R, and SQL, and expertise in machine learning, data visualization, and cloud technologies. Proficient in developing applications using FastAPI and Flask, with a strong background in Agile development and collaborative problem-solving. Eager to contribute to innovative projects and grow professionally in a dynamic environment.</p>
    </header>
    
        <section><h2>EXPERIENCE</h2>
        <div style="display: flex; justify-content: space-between; margin-top: 0;">
            <p><strong>Data Scientist - <i>Nexum-AI Consulting</i></strong></p>
            <p>Nov 2022 to now</p>
        </div>
        <li style="text-align: justify;">Automated daily Excel updates on SFTP server, reducing manual effort by 80% and ensuring timely data availability for stakeholders by utilizing Apache Beam, GCP dataflow, and firestore.</li><li style="text-align: justify;">Executed HR and IT chatbots with 5 language support on Streamlit based on Llama2, hosted on Google Cloud Compute Engine.</li><li style="text-align: justify;">Spearheaded a Natural Language Processing initiative, achieving a remarkable 90% accuracy in evaluating summarized text against the main text.</li><li style="text-align: justify;">Led cross-functional team to deploy VertexAI for forecasting and classification tasks, developing 50 APIs for seamless model integration, showcasing Python and cloud proficiency.</li></ul>
        <div style="display: flex; justify-content: space-between; margin-top: 0;">
            <p><strong>Data Scientist - <i>Dirac Nanotechnology</i></strong></p>
            <p>Feb 2020 to Oct 2022</p>
        </div>
        <li style="text-align: justify;">Appointed time series modeling on air pollution data, elevating prediction accuracy by 20% and empowering data-driven decisions to mitigate environmental impact.</li><li style="text-align: justify;">Implemented cutting edge technology to conduct high resolution air pollution mapping for 20 cities, resulting in localized insights that informed strategic environmental interventions and enhanced public health outcomes significantly.</li><li style="text-align: justify;">Directed social media trend analysis initiative, leveraging insights to optimize content strategy; boosted online engagement by 25%, leading to a 15% growth in customer acquisition and a 30% increase in brand awareness.</li><li style="text-align: justify;">Directed web scraping and data mining projects to tailor marketing approaches, achieving a 50% growth in lead generation.</li></ul></section>
        <section><h2>EDUCATION</h2>
        <div style="display: flex; justify-content: space-between; margin-top: 0;">
            <p><strong>Master in Data Science - <i>Sapienza University of Rome</i></strong></p>
            <p>Jan 2019 to Dec 2022</p>
        </div>
        <p style="margin-top: 0px; text-align: justify;">Thesis: Automatic extraction and integration of bibliographic data on Italian universities: focusing on web scraping to analyze publications from 90 Italian institutions on Scopus, extracting data and analyzing important keywords using NLP technique, and presenting results in dashboards.</p>
        
        <div style="display: flex; justify-content: space-between; margin-top: 0;">
            <p><strong>Bachelor in Information Technology - <i>Evanakey university</i></strong></p>
            <p>Sep 2010 to Sep 2014</p>
        </div>
        <p style="margin-top: 0px; text-align: justify;">Thesis: Cloud Computing: Evolution, Architecture, and Applications: Analyzed the evolution, architecture, and applications of cloud computing, focusing on its impact on business operations and IT infrastructure. Explored cloud service models (IaaS, PaaS, SaaS) and deployment models (public, private, hybrid).</p>
        </section>
        <section><h2>CERTIFICATES</h2>
        <h3 style="margin-top: 0; margin-bottom: 0;"><i>Google Cloud</i></h3>
        <div style="display: flex; justify-content: space-between; margin-bottom: 0;">
            <h3>Google Cloud Professional Machine Learning Engineer</h3>
            <p>Dec 2023</p>
        </div>
        <p style="margin-top: 0px; text-align: justify;">Frame ML problems, develop ML models, architect ML solutions, automate and orchestrate ML pipelines, design data preparation and processing systems, monitor, optimize, and maintain ML solutions.</p>
        
        <h3 style="margin-top: 0; margin-bottom: 0;"><i>Google Cloud</i></h3>
        <div style="display: flex; justify-content: space-between; margin-bottom: 0;">
            <h3>Google Cloud Professional Data Engineer</h3>
            <p>May 2023</p>
        </div>
        <p style="margin-top: 0px; text-align: justify;">Design data processing systems, build and operationalize data processing systems, operationalize machine learning models, ensure solution quality.</p>
        
        <h3 style="margin-top: 0; margin-bottom: 0;"><i>Amazon AWS</i></h3>
        <div style="display: flex; justify-content: space-between; margin-bottom: 0;">
            <h3>Amazon AWS Cloud Technical Essentials</h3>
            <p>Apr 2022</p>
        </div>
        <p style="margin-top: 0px; text-align: justify;">Understand the terminology and concepts related to the AWS platform, navigate the AWS Management Console, understand fundamental AWS Security Measures and AWS Identity and Access Management (IAM).</p>
        
        <h3 style="margin-top: 0; margin-bottom: 0;"><i>EDX</i></h3>
        <div style="display: flex; justify-content: space-between; margin-bottom: 0;">
            <h3>The Analytics Edge</h3>
            <p>Oct 2021</p>
        </div>
        <p style="margin-top: 0px; text-align: justify;">Gain an applied understanding of many different analytics methods, including linear regression, logistic regression, CART, clustering, and data visualization. Learn how to implement all of these methods in R. Understand mathematical optimization and how to solve optimization models in spreadsheet software.</p>
        </section>
        <section><h2>PROJECTS</h2>
        <h3>Llama 2 Chatbot</h3>
        <ul>
            <li style="text-align: justify;">Create a customizable and dynamic Llama 2 Chatbot for seamless interactions.</li>
            <li style="text-align: justify;">Integrate the chatbot with various platforms for enhanced user experience.</li>
            <li style="text-align: justify;">A fully functional Llama 2 Chatbot that can be customized and integrated with various platforms.</li>
        </ul>
        
        <h3>GCP Exam Questions Extractor</h3>
        <ul>
            <li style="text-align: justify;">Develop a Python tool using Selenium and BeautifulSoup to extract GCP exam Q&A.</li>
            <li style="text-align: justify;">Enhance the tool's functionality by adding features such as question filtering and answer validation.</li>
            <li style="text-align: justify;">A Python tool that can extract GCP exam Q&A and provide additional features for enhanced user experience.</li>
        </ul>
        
        <h3>AI CV Generator</h3>
        <ul>
            <li style="text-align: justify;">Create an AI-driven tool to optimize CVs for precise job alignment.</li>
            <li style="text-align: justify;">Integrate the tool with various job platforms for seamless job application.</li>
            <li style="text-align: justify;">An AI-driven tool that can optimize CVs for precise job alignment and integrate with various job platforms.</li>
        </ul>
        
        <h3>IOT Analysis Dashboard</h3>
        <ul>
            <li style="text-align: justify;">Develop a Streamlit dashboard for data visualization, including real-time metrics and error logs.</li>
            <li style="text-align: justify;">Integrate the dashboard with various IoT devices for real-time data analysis.</li>
            <li style="text-align: justify;">A Streamlit dashboard that can visualize real-time data and error logs from various IoT devices.</li>
        </ul>
        </section>
        
        <section><h2>SKILLS</h2><h3>Hard Skills</h3><ul><li style="text-align: justify;">Python ,  R ,  SQL ,  FastAPI ,  Git ,  Docker ,  Pandas ,  scikit-learn ,  Pytorch ,  Apache Beam ,  Beautiful Soup ,  Selenium ,  Streamlit ,  NLTK ,  Seaborn ,  Tableau ,  GCP BigQuery ,  GCP VertexAI ,  GCP Dataflow ,  GCP AutoML ,  GCP Dialogflow ,  GCP Pub/Sub ,  OpenAI ,  Llama2 ,  Hugging Face ,  MongoDB ,  Firebase ,  MySQL</li></ul><h3>Soft Skills</h3><ul><li style="text-align: justify;">Collaboration ,  Cross-functional teamwork ,  Data analysis ,  Data preprocessing ,  Data visualization ,  Experiment design ,  Experiment evaluation ,  Predictive modeling ,  Machine learning ,  Problem-solving ,  Continuous learning ,  Professional growth ,  Written communication ,  Verbal communication ,  Independent work ,  Teamwork ,  Adaptability ,  Knowledge sharing ,  Documentation ,  Research</li></ul></section>
        
    </body>
    </html>
"""

def perfect_css_style(color_code : str) -> str:
    css = f"""
    body {{
        font-family: 'Times New Roman', Times, serif;
        font-size: 14px;
        line-height: 1.5;
        background-color: #ffffff;
        margin: -5px;
        margin-top: -50px;
        padding: 0;
        padding-top: 0px;
    }}

    header, section {{
        padding: 10px 20px;
        margin-top: 0;
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
        margin-top: 30px;
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


color_code="#000000"
font_config = FontConfiguration()
html = HTML(string=f"""{data_html}""")
css = CSS(string=f'''{perfect_css_style(color_code)}''', font_config=font_config)
html.write_pdf('test.pdf', stylesheets=[css], font_config=font_config)

