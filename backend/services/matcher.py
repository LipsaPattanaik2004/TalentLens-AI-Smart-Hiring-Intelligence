from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_skills():
    with open("data/skills.json") as f:
        return json.load(f)

def extract_skills(text, skills_list):
    return [skill for skill in skills_list if skill in text]

def match_resume_jd(resume, jd):
    skills = load_skills()

    resume_skills = extract_skills(resume, skills)
    jd_skills = extract_skills(jd, skills)

    missing = list(set(jd_skills) - set(resume_skills))

    score = util.cos_sim(
        model.encode(resume),
        model.encode(jd)
    ).item()

    return {
        "match_score": round(score * 100, 2),
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "missing_skills": missing
    }
