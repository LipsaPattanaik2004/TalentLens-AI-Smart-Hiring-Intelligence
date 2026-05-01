from fastapi import APIRouter, UploadFile, File
from backend.services.parser import extract_text
from backend.services.matcher import match_resume_jd
from backend.services.feedback import generate_feedback

router = APIRouter()

@router.post("/analyze")
async def analyze(resume: UploadFile = File(...), jd: UploadFile = File(...)):
    resume_text = extract_text(await resume.read())
    jd_text = extract_text(await jd.read())

    result = match_resume_jd(resume_text, jd_text)
    feedback = generate_feedback(result["match_score"], result["missing_skills"])

    return {
        "analysis": result,
        "feedback": feedback
    }
