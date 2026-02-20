import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Felix Christian Go | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Merriweather:wght@700&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Inter', sans-serif;
    background-color: #0d1117;
    color: #c9d1d9;
}

h1, h2, h3 {
    font-family: 'Merriweather', serif;
    color: #e6edf3;
}

section[data-testid="stSidebar"] {
    background-color: #0d1117;
    border-right: 1px solid #21262d;
}
section[data-testid="stSidebar"] * {
    color: #c9d1d9 !important;
}
section[data-testid="stSidebar"] .stRadio label {
    font-size: 0.95rem;
    padding: 4px 0;
}

.hero {
    background: linear-gradient(135deg, #0d1117 0%, #161b22 50%, #1a2332 100%);
    border-radius: 14px;
    padding: 52px 48px 48px 48px;
    margin-bottom: 24px;
    border: 1px solid #21262d;
}
.hero .role {
    font-size: 0.78rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #58a6ff;
    margin-bottom: 16px;
    font-weight: 400;
}
.hero h1 {
    font-size: 3rem;
    color: #e6edf3;
    margin: 0 0 20px 0;
    line-height: 1.15;
}
.hero .bio {
    font-size: 0.95rem;
    color: #8b949e;
    line-height: 1.75;
    max-width: 620px;
}

.stat-box {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 12px;
    padding: 28px 20px;
    text-align: center;
}
.stat-box .num {
    font-family: 'Merriweather', serif;
    font-size: 2.2rem;
    color: #58a6ff;
    line-height: 1;
}
.stat-box .lbl {
    font-size: 0.78rem;
    color: #8b949e;
    margin-top: 8px;
    letter-spacing: 0.5px;
}

.card {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 12px;
    padding: 24px 28px;
    margin-bottom: 16px;
}
.card-title {
    font-family: 'Merriweather', serif;
    font-size: 1.05rem;
    color: #e6edf3;
    margin-bottom: 4px;
}
.card-sub {
    font-size: 0.8rem;
    color: #8b949e;
    margin-bottom: 12px;
}
.card p {
    font-size: 0.92rem;
    line-height: 1.7;
    color: #8b949e;
    margin: 0;
}

.section-header {
    font-family: 'Merriweather', serif;
    font-size: 1.45rem;
    color: #e6edf3;
    border-bottom: 1px solid #21262d;
    padding-bottom: 10px;
    margin-bottom: 20px;
    margin-top: 8px;
}

.tag {
    display: inline-block;
    background: #1f3048;
    color: #58a6ff;
    border: 1px solid #1f4068;
    border-radius: 4px;
    padding: 4px 12px;
    font-size: 0.8rem;
    margin: 3px 3px;
    font-weight: 500;
}

.cert-tag {
    display: inline-block;
    background: #1a2d1a;
    color: #3fb950;
    border: 1px solid #2ea043;
    border-radius: 4px;
    padding: 4px 12px;
    font-size: 0.8rem;
    margin: 3px 3px;
    font-weight: 500;
}

.contact-row {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 8px;
    padding: 14px 20px;
    margin-bottom: 10px;
    font-size: 0.92rem;
    color: #c9d1d9;
}

div[data-testid="stForm"] {
    background: #161b22;
    border: 1px solid #21262d;
    border-radius: 12px;
    padding: 24px;
}

.stTextInput input, .stTextArea textarea {
    background-color: #0d1117 !important;
    border: 1px solid #30363d !important;
    color: #c9d1d9 !important;
    border-radius: 6px !important;
}
.stTextInput label, .stTextArea label {
    color: #8b949e !important;
    font-size: 0.87rem !important;
}

.stButton button {
    background-color: #238636 !important;
    color: white !important;
    border: none !important;
    border-radius: 6px !important;
    font-weight: 500 !important;
}
.stButton button:hover {
    background-color: #2ea043 !important;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### Felix Christian Go")
    st.markdown("<span style='font-size:0.82rem;color:#8b949e;'>Student Developer</span>", unsafe_allow_html=True)
    st.divider()
    page = st.radio(
        "Navigate",
        ["Home", "About Me", "Projects", "Skills", "Certifications", "Contact"],
        label_visibility="collapsed"
    )
    st.divider()
    st.markdown("<span style='font-size:0.8rem;color:#8b949e;'>4th Year BSIT · CIT-University<br>Cebu, Philippines</span>", unsafe_allow_html=True)


if page == "Home":
    st.markdown("""
    <div class="hero">
        <div class="role">Student Developer</div>
        <h1>Felix Christian Go</h1>
        <p class="bio">
            4th Year BSIT undergraduate with growing knowledge in programming.
            Experienced in developing academic projects using modern tools and technologies.
            Eager to gain hands-on experience in the IT field and contribute to real-world
            solutions while continuing to expand my skills.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    stats = [("2", "Academic Projects"), ("3+", "AWS Certifications"), ("3", "Years in BSIT"), ("5+", "Technologies Used")]
    for col, (num, label) in zip([c1, c2, c3, c4], stats):
        with col:
            st.markdown(f"""
            <div class="stat-box">
                <div class="num">{num}</div>
                <div class="lbl">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">Education</div>
            <div class="card-sub">Cebu Institute of Technology - University</div>
            <p>Bachelor of Science in Information Technology &nbsp;&middot;&nbsp; 2023 – Present</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">Current Focus</div>
            <div class="card-sub">Frontend Development</div>
            <p>Building modern web applications using React JS + Vite, integrating with Spring Boot backends and cloud technologies.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("Use the sidebar to navigate through the different sections of this portfolio.")


elif page == "About Me":
    st.markdown('<div class="section-header">About Me</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="card">
            <p>
            Hi, I'm <strong style="color:#e6edf3;">Felix Christian Go</strong>, a 4th Year Bachelor of Science in Information Technology
            student at <strong style="color:#e6edf3;">Cebu Institute of Technology – University</strong>. I have a passion for building
            clean, user-friendly web applications and solving real-world problems through technology.
            <br><br>
            My journey in IT has exposed me to the full development lifecycle — from designing responsive
            frontends to integrating backend APIs and managing databases. I am always eager to learn new tools
            and frameworks that help me grow as a developer.
            <br><br>
            I value teamwork, effective communication, and continuous learning — qualities I bring into every
            project I am part of.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">Personal Info</div>
            <br>
            <p><span style="color:#58a6ff;">Name</span><br><span style="color:#e6edf3;">Felix Christian Go</span></p><br>
            <p><span style="color:#58a6ff;">Year Level</span><br><span style="color:#e6edf3;">4th Year BSIT</span></p><br>
            <p><span style="color:#58a6ff;">School</span><br><span style="color:#e6edf3;">CIT-University</span></p><br>
            <p><span style="color:#58a6ff;">Location</span><br><span style="color:#e6edf3;">Minglanilla, Cebu</span></p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-header" style="margin-top:24px;">Education</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div class="card-title">Bachelor of Science in Information Technology</div>
        <div class="card-sub">Cebu Institute of Technology - University &nbsp;|&nbsp; 2023 – 2026</div>
        <p>Currently in 4th year, with focus on web and backend development, cloud computing, and software engineering practices.</p>
    </div>
    """, unsafe_allow_html=True)


elif page == "Projects":
    st.markdown('<div class="section-header">Academic Projects</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-title">Teacher Attendance Checker System (TACS)</div>
        <div class="card-sub">Frontend Developer &nbsp;&middot;&nbsp; 2025</div>
        <p>
        Developed user-friendly web pages for a student attendance management system used by teachers to track and manage class attendance.
        Integrated the user interface with backend systems to display real-time data such as student lists, course information, and attendance records.
        Collaborated with team members using GitHub to track changes and manage code contributions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-title">Software Testing Document Evaluator</div>
        <div class="card-sub">Frontend Developer &nbsp;&middot;&nbsp; 2025 – Present</div>
        <p>
        Developed user-facing web pages for an AI-powered educational platform that helps students and teachers evaluate software testing documents.
        Built interactive dashboards showing usage statistics, submission history, and evaluation reports for both students and teachers.
        Created teacher tools for reviewing student work, overriding AI scores when needed, and viewing class performance analytics.
        Collaborated with backend developers using GitHub to manage code changes and coordinate feature integration.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-header" style="margin-top:24px;">Technologies Used</div>', unsafe_allow_html=True)
    techs = ["React JS", "Vite", "HTML", "CSS", "Spring Boot", "MySQL", "PostgreSQL", "GitHub", "Postman"]
    st.markdown("".join(f'<span class="tag">{t}</span>' for t in techs), unsafe_allow_html=True)

    st.markdown("<br>**Role Breakdown**", unsafe_allow_html=True)
    st.progress(0.90, text="Frontend Development — 90%")
    st.progress(0.60, text="UI/UX Design — 60%")
    st.progress(0.50, text="API Integration — 50%")
    st.progress(0.70, text="Team Collaboration — 70%")


elif page == "Skills":
    st.markdown('<div class="section-header">Skills & Technologies</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card"><div class="card-title">Frontend Development</div><br>', unsafe_allow_html=True)
        for skill, val in {"HTML": 80, "CSS": 75, "React JS + Vite": 70}.items():
            st.progress(val / 100, text=f"{skill} — {val}%")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-title">Tools</div><br>', unsafe_allow_html=True)
        st.markdown("".join(f'<span class="tag">{t}</span>' for t in ["GitHub", "VS Code", "Postman"]), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><div class="card-title">Backend & Database</div><br>', unsafe_allow_html=True)
        for skill, val in {"Spring Boot": 60, "MySQL": 65, "PostgreSQL": 60}.items():
            st.progress(val / 100, text=f"{skill} — {val}%")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-title">Soft Skills</div><br>', unsafe_allow_html=True)
        st.markdown("".join(f'<span class="tag">{s}</span>' for s in ["Teamwork", "Communication", "Problem Solving", "Adaptability"]), unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section-header" style="margin-top:24px;">Skill Summary</div>', unsafe_allow_html=True)
    df = pd.DataFrame({
        "Proficiency (%)": [80, 75, 70, 60, 65, 60, 75]
    }, index=["HTML", "CSS", "React JS", "Spring Boot", "MySQL", "PostgreSQL", "GitHub"])
    st.bar_chart(df)


elif page == "Certifications":
    st.markdown('<div class="section-header">Certifications</div>', unsafe_allow_html=True)

    certs = [
        ("AWS Academy – AWS for Beginners", "Amazon Web Services (AWS Academy)", "Foundational cloud literacy covering core AWS services and use cases."),
        ("AWS Academy Cloud Foundations", "Amazon Web Services (AWS Academy)", "Comprehensive overview of cloud concepts, AWS core services, security, architecture, and pricing."),
        ("AWS Academy Cloud Architecting", "Amazon Web Services (AWS Academy)", "Advanced course on designing fault-tolerant and scalable AWS architectures."),
        ("ASEAN AI Literacy Training", "ASEAN Foundation", "AI literacy program covering fundamentals of artificial intelligence and its applications in Southeast Asia."),
    ]

    for title, issuer, desc in certs:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{title}</div>
            <div class="card-sub">{issuer}</div>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-header" style="margin-top:24px;">Certification Areas</div>', unsafe_allow_html=True)
    st.markdown("".join(f'<span class="cert-tag">{c}</span>' for c in ["Cloud Computing", "AWS", "AI & Machine Learning", "Cloud Architecture", "Cloud Security"]), unsafe_allow_html=True)


elif page == "Contact":
    st.markdown('<div class="section-header">Get In Touch</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])
    with col1:
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message", height=150)
            submitted = st.form_submit_button("Send Message", use_container_width=True)

            if submitted:
                if name and email and message:
                    st.success(f"Thank you, {name}. Your message has been sent.")
                else:
                    st.warning("Please fill in all required fields.")

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">Contact Details</div>
            <br>
            <span style="color:#58a6ff;">Phone Number</span><br><div class="contact-row">(+63) 992 733 0569</div>
            <span style="color:#58a6ff;">Email</span><br><div class="contact-row">go.felixchristian@gmail.com</div>
            <span style="color:#58a6ff;">Address</span><br><div class="contact-row">Deca Homes Phase 1, Tungkil, Minglanilla, Cebu</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <div class="card-title">Open to Opportunities</div>
            <br>
            <p>Feel free to reach out via email for collaborations, internship opportunities, or any inquiries.</p>
        </div>
        """, unsafe_allow_html=True)