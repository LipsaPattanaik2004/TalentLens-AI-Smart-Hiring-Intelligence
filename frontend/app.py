import streamlit as st
import requests

st.title("TalentLens AI")

resume = st.file_uploader("Upload Resume (PDF)")
jd = st.file_uploader("Upload Job Description (PDF)")

if st.button("Analyze"):
    if resume and jd:
        files = {
            "resume": resume,
            "jd": jd
        }

        response = requests.post("http://127.0.0.1:8000/analyze", files=files)
        data = response.json()

        st.subheader("Match Score")
        st.write(data["analysis"]["match_score"])

        st.subheader("Missing Skills")
        st.write(data["analysis"]["missing_skills"])

        st.subheader("Feedback")
        st.write(data["feedback"]["summary"])
        st.write(data["feedback"]["suggestions"])

        q = requests.post(
            "http://127.0.0.1:8000/questions",
            json=data["analysis"]
        )

        st.subheader("Interview Questions")
        st.write(q.json()["questions"])
