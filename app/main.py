from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import APP_NAME
from app.database.database import engine, Base
from app.models.student import Student
from app.models.user import User
from app.routers.auth import router as auth_router

from app.routers.students import router as student_router
from app.routers.ai import router as ai_router
from app.models.chat import ChatMessage
from app.routers.rag import router as rag_router


# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI application
app = FastAPI(
    title=APP_NAME
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Student AI Platform"
    }


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "Student AI Platform is running"
    }


# Include Student APIs
app.include_router(student_router)


# Include AI APIs
app.include_router(ai_router)


# Include RAG APIs
app.include_router(rag_router)

app.include_router(auth_router)