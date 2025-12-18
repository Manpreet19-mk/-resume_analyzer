
import streamlit as st
import os
import tempfile

from utils.pdf_parser import extract_text_from_pdf
from utils.skill_extractor import load_skills, extract_skills
from utils.scorer import calculate_score

# -------- CONFIG --------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SKILLS_FILE = os.path.join(BASE_DIR, "utils", "data", "skills_list.txt")

# -------- PAGE CONFIG --------
st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# -------- HEADER --------
st.title("📄 Resume Analyzer")
st.caption("Analyze how well a resume matches a job description")

st.markdown("---")

# -------- INPUT SECTION --------
st.subheader("📥 Input")

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

with col2:
    jd_text = st.text_area(
        "Paste Job Description",
        height=180,
        placeholder="Paste the job description here..."
    )

analyze_btn = st.button("🔍 Analyze Resume", use_container_width=True)

st.markdown("---")

# -------- LOGIC --------
if analyze_btn:
    if resume_file is None:
        st.error("Please upload a resume PDF.")
    elif not jd_text.strip():
        st.error("Please paste a job description.")
    else:
        with st.spinner("Analyzing resume..."):
            # Save resume temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(resume_file.read())
                resume_path = tmp.name

            # Load skills
            skills = load_skills(SKILLS_FILE)

            # Extract text
            resume_text = extract_text_from_pdf(resume_path)
            jd_text = jd_text.lower()

            # Extract skills
            resume_skills = extract_skills(resume_text, skills)
            jd_skills = extract_skills(jd_text, skills)

            matched_skills = resume_skills.intersection(jd_skills)
            score = calculate_score(matched_skills)

            os.remove(resume_path)

        # -------- OUTPUT --------
        st.subheader("✅ Results")

        # Score metric
        st.metric(
            label="Matched Skills Count",
            value=len(matched_skills)
        )

        # Skills display
        st.markdown("### 🧠 Matched Skills")

        if matched_skills:
            skill_cols = st.columns(3)
            for i, skill in enumerate(sorted(matched_skills)):
                skill_cols[i % 3].success(skill)
        else:
            st.info("No skills matched between resume and job description.")
