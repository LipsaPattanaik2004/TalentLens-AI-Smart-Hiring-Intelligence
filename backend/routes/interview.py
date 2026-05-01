from fastapi import APIRouter
from backend.services.question_generator import generate_questions

router = APIRouter()

@router.post("/questions")
def generate(data: dict):
    missing_skills = data.get("missing_skills", [])
    questions = generate_questions(missing_skills)

    return {"questions": questions}
