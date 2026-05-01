def generate_feedback(score, missing_skills):
    suggestions = []

    for skill in missing_skills:
        suggestions.append(f"Improve your knowledge in {skill}")

    return {
        "score": score,
        "summary": "Good match" if score > 70 else "Needs improvement",
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }
