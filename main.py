app = FastAPI()

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from pathlib import Path

from resume_matcher import analyze_resume

app = FastAPI(title="AI Resume Analyzer")

BASE_DIR = Path(__file__).resolve().parent


class ResumeRequest(BaseModel):
    resume: str
    job_description: str


@app.get("/")
def home():
    index_file = BASE_DIR / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return {"message": "AI Resume Analyzer API is running"}


@app.post("/analyze")
def analyze(request: ResumeRequest):
    if not request.resume.strip():
        return {"error": "Resume text cannot be empty"}

    if not request.job_description.strip():
        return {"error": "Job description cannot be empty"}

    result = analyze_resume(
        request.resume,
        request.job_description
    )

    return result


@app.get("/health")
def health():
    return {"status": "healthy"}
