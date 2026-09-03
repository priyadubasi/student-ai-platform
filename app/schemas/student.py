from pydantic import BaseModel, Field
from typing import Optional


# CREATE student
class Student(BaseModel):

    name: str = Field(
        ...,
        min_length=2,
        max_length=50
    )

    department: str = Field(
        ...,
        min_length=2,
        max_length=20
    )

    year: int = Field(
        ...,
        ge=1,
        le=4
    )


# UPDATE student
class StudentUpdate(BaseModel):

    name: Optional[str] = Field(
        None,
        min_length=2,
        max_length=50
    )

    department: Optional[str] = Field(
        None,
        min_length=2,
        max_length=20
    )

    year: Optional[int] = Field(
        None,
        ge=1,
        le=4
    )


# RESPONSE
class StudentResponse(BaseModel):

    id: int
    name: str
    department: str
    year: int
    
    # DELETE response
class MessageResponse(BaseModel):

    message: str