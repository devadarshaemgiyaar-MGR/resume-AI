
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def analyze_resume(resume, job_description):
    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform([
        resume,
        job_description
    ])

    score = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    skills = [
        "python", "java", "sql", "html",
        "css", "javascript", "fastapi",
        "machine learning", "pandas",
        "spring boot"
    ]

    resume_lower = resume.lower()
    job_lower = job_description.lower()

    resume_skills = [
        skill for skill in skills
        if skill in resume_lower
    ]

    required_skills = [
        skill for skill in skills
        if skill in job_lower
    ]

    matched = [
        skill for skill in required_skills
        if skill in resume_skills
    ]

    missing = [
        skill for skill in required_skills
        if skill not in resume_skills
    ]

    return {
        "match_percentage": round(score * 100, 2),
        "matched_skills": matched,
        "missing_skills": missing
    }


if __name__ == "__main__":
    resume = input("Paste resume text: ")
    job = input("Paste job description: ")

    result = analyze_resume(resume, job)
    print(result)