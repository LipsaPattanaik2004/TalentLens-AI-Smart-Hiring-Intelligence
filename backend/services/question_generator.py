def generate_questions(missing_skills):
    questions = []

    for skill in missing_skills:
        questions.append(f"Explain your experience with {skill}.")

    if not questions:
        questions.append("Describe your strongest project.")

    return questions
