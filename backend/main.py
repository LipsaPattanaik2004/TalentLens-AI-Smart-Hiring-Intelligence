from fastapi import FastAPI
from backend.routes import analyze, interview

app = FastAPI(title="TalentLens AI")

app.include_router(analyze.router)
app.include_router(interview.router)

@app.get("/")
def home():
    return {"message": "TalentLens AI Running"}
