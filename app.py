import streamlit as st
import utils
import prompts

st.title("Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    resume_text = utils.extract_text_from_document(uploaded_file)

    st.subheader("Skills Extracted:")
    skills = utils.extract_skills(resume_text)
    st.write(skills)

    st.subheader("Formatting Feedback:")
    formatting_feedback = utils.get_formatting_feedback(resume_text)
    st.write(formatting_feedback)

    st.subheader("Content Suggestions:")
    content_suggestions = utils.get_content_suggestions(resume_text)
    st.write(content_suggestions)

    # Optional: Job Description Input
    job_description = st.text_area("Paste Job Description (Optional)")
    if job_description:
        keyword_analysis = utils.analyze_keywords(resume_text, job_description)
        st.subheader("Keyword Analysis:")
        st.write(keyword_analysis)