# app.py

import streamlit as st
import os
from dotenv import load_dotenv
from utils.analyzer import (
    review_resume,
    extract_skills,
    match_percentage,
    generate_cover_letter,
)
from utils.parser import extract_text_from_pdf
from utils.visualizer import plot_skill_match, generate_pdf_report

# --- Streamlit Page Config ---
st.set_page_config(page_title="ATS Resume Scanner", layout="centered", page_icon="🔍")

# --- Load Environment Variables ---
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# --- App Title ---
st.markdown("<h1 style='text-align: center;'>🔍 ATS Resume Scanner Pro</h1>", unsafe_allow_html=True)
st.caption("AI-powered resume and job description analysis tool using Google Gemini")

# --- File Upload & Job Description ---
uploaded_resume = st.file_uploader("📄 Upload your resume (PDF only):", type=["pdf"])
job_description = st.text_area("📝 Paste the Job Description here:")

# --- Initialize Session State ---
if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

# --- Resume Text Extraction ---
if uploaded_resume:
    try:
        with st.spinner("Extracting text from resume..."):
            st.session_state.resume_text = extract_text_from_pdf(uploaded_resume)
        st.success("✅ Resume parsed successfully!")
        st.text_area("📜 Extracted Resume Text", st.session_state.resume_text, height=200)
    except Exception as e:
        st.error(f"❌ Failed to parse resume: {e}")

# --- AI Analysis Tools ---
if st.session_state.resume_text.strip() and job_description.strip():
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("🔍 AI Analysis Tools")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📊 Resume Evaluation"):
            with st.spinner("Analyzing resume..."):
                result = review_resume(st.session_state.resume_text, job_description)
                st.success("✅ Analysis Complete")
                st.write(result)

    with col2:
        if st.button("🧠 Extract Skills"):
            with st.spinner("Extracting skills..."):
                result = extract_skills(st.session_state.resume_text, job_description)
                if isinstance(result, dict) and all(k in result for k in ["Technical Skills", "Analytical Skills", "Soft Skills"]):
                    st.subheader("🧠 Extracted Skills")
                    for skill_type in ["Technical Skills", "Analytical Skills", "Soft Skills"]:
                        skills = result.get(skill_type, [])
                        if skills:
                            st.markdown(f"**{skill_type}:**")
                            st.write(", ".join(skills))
                        else:
                            st.markdown(f"**{skill_type}:** ❌ *No skills found*")
                    st.subheader("📊 Skill Match Radar Chart")
                    plot_skill_match(result)
                else:
                    st.error("❌ Skill extraction failed.")
                    st.code(result if isinstance(result, str) else result.get("raw_response", "No raw response"))

    with col3:
        if st.button("✅ Match Score"):
            with st.spinner("Calculating match percentage..."):
                result = match_percentage(st.session_state.resume_text, job_description)
                st.success("✅ Scoring Complete")
                st.write(result)
else:
    st.info("📌 Please upload a resume and job description to proceed.")

# --- Cover Letter Generator ---
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("✉️ Generate AI Cover Letter")
your_name = st.text_input("👤 Your Name", placeholder="Pankaj Mantri")

if st.button("✉️ Generate Cover Letter"):
    if st.session_state.resume_text.strip() and job_description.strip():
        with st.spinner("Generating your cover letter..."):
            letter = generate_cover_letter(st.session_state.resume_text, job_description, your_name or "Pankaj Mantri")
            st.session_state.cover_letter = letter
            st.text_area("📬 Your Cover Letter:", letter, height=300)
            st.download_button("📥 Download Cover Letter", letter, file_name="cover_letter.txt")
    else:
        st.warning("📌 Resume and Job Description required.")

# --- PDF Report Generator ---
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("📥 Download Full Analysis Report")

if st.session_state.resume_text.strip() and job_description.strip():
    candidate_name = st.text_input("Your Name (for report):", placeholder="Pankaj Mantri", key="report_name")
    if st.button("🧾 Generate PDF Report"):
        with st.spinner("Preparing your report..."):
            eval_text = review_resume(st.session_state.resume_text, job_description)
            skills_data = extract_skills(st.session_state.resume_text, job_description)
            match_result = match_percentage(st.session_state.resume_text, job_description)
            cover_letter_text = st.session_state.get("cover_letter", "")
            pdf_bytes = generate_pdf_report(
                name=candidate_name or "Anonymous",
                evaluation=eval_text,
                skills_dict=skills_data if isinstance(skills_data, dict) else {},
                match_score_text=match_result,
                cover_letter=cover_letter_text
            )
            st.download_button("📩 Download Report as PDF", data=pdf_bytes, file_name="ATS_Resume_Report.pdf", mime="application/pdf")
else:
    st.warning("📌 Resume and Job Description required to generate the report.")
