from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.rag_service import ask_rag


router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


from pydantic import BaseModel, Field


class RAGRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=500
    )

@router.post("/ask")
def ask_question(data: RAGRequest):

    answer = ask_rag(data.question)

    return {
        "question": data.question,
        "answer": answer
    }