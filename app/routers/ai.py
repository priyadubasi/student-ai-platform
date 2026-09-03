from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.services.ai_service import (
    ask_ai,
    chat_with_history
)

from app.database.database import get_db
from app.models.student import Student


router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


# ============================================================
# 1. BASIC AI QUESTION
# ============================================================

class AIRequest(BaseModel):
    question: str


class AIResponse(BaseModel):
    answer: str


@router.post("/ask", response_model=AIResponse)
def ask_question(request: AIRequest):

    prompt = f"""
You are a helpful AI Student Assistant.

Your job is to help students with:
- Academic subjects
- Programming
- Data Science
- Artificial Intelligence
- Machine Learning
- Career preparation
- Placement preparation

Give simple, clear and accurate answers.

Student Question:
{request.question}
"""

    answer = ask_ai(prompt)

    return {
        "answer": answer
    }


# ============================================================
# 2. AI STUDY PLAN
# ============================================================

class StudyPlanRequest(BaseModel):
    subject: str
    days: int


class StudyPlanResponse(BaseModel):
    study_plan: str


@router.post("/study-plan", response_model=StudyPlanResponse)
def generate_study_plan(request: StudyPlanRequest):

    prompt = f"""
You are an AI Study Plan Generator.

Create a practical and beginner-friendly study plan
for a student.

Subject: {request.subject}
Number of Days: {request.days}

Requirements:
- Divide the plan day by day.
- Give topics to study each day.
- Include practice activities.
- Include revision.
- Keep the plan realistic.
- Use simple language.
- Give a clear structured response.

Generate the study plan now.
"""

    study_plan = ask_ai(prompt)

    return {
        "study_plan": study_plan
    }


# ============================================================
# 3. STUDENT PERFORMANCE ANALYSIS
# ============================================================

class PerformanceRequest(BaseModel):
    student_name: str
    marks: dict[str, float]


class PerformanceResponse(BaseModel):
    analysis: str


@router.post("/performance", response_model=PerformanceResponse)
def analyze_performance(request: PerformanceRequest):

    marks_text = "\n".join(
        f"{subject}: {mark}"
        for subject, mark in request.marks.items()
    )

    prompt = f"""
You are an AI Student Performance Analyzer.

Analyze the following student's academic performance.

Student Name: {request.student_name}

Marks:
{marks_text}

Provide:
1. Overall performance summary
2. Strong subjects
3. Subjects that need improvement
4. Study recommendations
5. Practical next steps

Use simple and encouraging language.

Do not make assumptions about information
that was not provided.
"""

    analysis = ask_ai(prompt)

    return {
        "analysis": analysis
    }


# ============================================================
# 4. ANALYZE STUDENT FROM DATABASE
# ============================================================

class StudentAnalysisResponse(BaseModel):
    student_id: int
    student_name: str
    analysis: str


@router.get(
    "/student/{student_id}",
    response_model=StudentAnalysisResponse
)
def analyze_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    prompt = f"""
You are an AI Student Assistant.

Analyze the following student profile:

Student ID: {student.id}
Student Name: {student.name}
Department: {student.department}
Year: {student.year}

Provide:
1. A short student profile summary
2. Suitable learning recommendations
3. Useful technical skills to learn
4. Career or placement preparation suggestions

Use simple and encouraging language.

Do not assume information that was not provided.
"""

    analysis = ask_ai(prompt)

    return {
        "student_id": student.id,
        "student_name": student.name,
        "analysis": analysis
    }


# ============================================================
# 5. ASK QUESTION ABOUT A STUDENT
# ============================================================

class StudentQueryRequest(BaseModel):
    student_id: int
    question: str


class StudentQueryResponse(BaseModel):
    student_id: int
    student_name: str
    answer: str


@router.post(
    "/student/query",
    response_model=StudentQueryResponse
)
def query_student(
    request: StudentQueryRequest,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(Student.id == request.student_id)
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    prompt = f"""
You are an AI Student Assistant.

Use ONLY the student information provided below
to answer the student's question.

Student Information:
Student ID: {student.id}
Name: {student.name}
Department: {student.department}
Year: {student.year}

Question:
{request.question}

Rules:
- Answer clearly and simply.
- Use the available student information.
- Do not invent information.
- If the information is not available,
  say that it is not available in the database.
"""

    answer = ask_ai(prompt)

    return {
        "student_id": student.id,
        "student_name": student.name,
        "answer": answer
    }


# ============================================================
# 6. STUDENT RECOMMENDATIONS
# ============================================================

class StudentRecommendationResponse(BaseModel):
    student_id: int
    student_name: str
    recommendations: str


@router.get(
    "/student/{student_id}/recommendations",
    response_model=StudentRecommendationResponse
)
def student_recommendations(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    prompt = f"""
You are an AI Student Career and Learning Assistant.

Student Profile:
Student ID: {student.id}
Name: {student.name}
Department: {student.department}
Year: {student.year}

Based only on the information provided,
give useful personalized recommendations.

Include:
1. Recommended technical skills
2. Recommended subjects to focus on
3. Project ideas suitable for the student
4. Placement preparation suggestions
5. A simple learning roadmap

Keep the recommendations practical,
clear, and encouraging.

Do not invent marks, skills, interests,
or experience that were not provided.
"""

    recommendations = ask_ai(prompt)

    return {
        "student_id": student.id,
        "student_name": student.name,
        "recommendations": recommendations
    }


# ============================================================
# 7. CONVERSATIONAL AI CHAT
# ============================================================

class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    session_id: str
    answer: str


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    answer = chat_with_history(
        db,
        request.session_id,
        request.message
    )

    return {
        "session_id": request.session_id,
        "answer": answer
    }