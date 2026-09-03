from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user import User
from app.routers.auth import (
    get_current_user,
    get_current_admin
)

from app.schemas.student import (
    Student,
    StudentUpdate,
    StudentResponse,
    MessageResponse
)

from app.services.student_service import (
    get_students,
    get_student_by_id,
    create_student,
    update_student,
    patch_student,
    delete_student
)


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# =========================
# GET ALL STUDENTS
# Any authenticated user
# =========================

@router.get(
    "/",
    response_model=list[StudentResponse]
)
def get_students_api(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    department: str | None = Query(None),
    year: int | None = Query(None, ge=1, le=4),
    name: str | None = Query(None),
    sort_by: str = Query("id"),
    order: str = Query("asc"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    students = get_students(
        db,
        skip,
        limit,
        department,
        year,
        name,
        sort_by,
        order
    )

    return students


# =========================
# GET SINGLE STUDENT
# Any authenticated user
# =========================

@router.get(
    "/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    student = get_student_by_id(
        db,
        student_id
    )

    if student is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student


# =========================
# CREATE STUDENT
# Admin only
# =========================

@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def add_student(
    student: Student,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):

    new_student = create_student(
        db,
        student
    )

    if new_student is None:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Student already exists"
        )

    return new_student


# =========================
# UPDATE COMPLETE STUDENT
# Admin only
# =========================

@router.put(
    "/{student_id}",
    response_model=StudentResponse
)
def update_student_api(
    student_id: int,
    updated_student: Student,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):

    student = update_student(
        db,
        student_id,
        updated_student
    )

    if student is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student


# =========================
# PATCH STUDENT
# Admin only
# =========================

@router.patch(
    "/{student_id}",
    response_model=StudentResponse
)
def patch_student_api(
    student_id: int,
    updated_data: StudentUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):

    student = patch_student(
        db,
        student_id,
        updated_data
    )

    if student is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return student


# =========================
# DELETE STUDENT
# Admin only
# =========================

@router.delete(
    "/{student_id}",
    response_model=MessageResponse,
    status_code=status.HTTP_200_OK
)
def delete_student_api(
    student_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):

    deleted = delete_student(
        db,
        student_id
    )

    if not deleted:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }