from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.models.student import Student as StudentModel
from app.schemas.student import Student, StudentUpdate


# GET all students
def get_students(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    department: str | None = None,
    year: int | None = None,
    name: str | None = None,
    sort_by: str = "id",
    order: str = "asc"
):

    try:

        query = db.query(StudentModel)

        # Name search
        if name is not None:

            query = query.filter(
                StudentModel.name.ilike(
                    f"%{name}%"
                )
            )

        # Department filter
        if department is not None:

            query = query.filter(
                StudentModel.department == department
            )

        # Year filter
        if year is not None:

            query = query.filter(
                StudentModel.year == year
            )

        # Sorting
        sort_columns = {
            "id": StudentModel.id,
            "name": StudentModel.name,
            "department": StudentModel.department,
            "year": StudentModel.year
        }

        sort_column = sort_columns.get(
            sort_by,
            StudentModel.id
        )

        if order == "desc":

            query = query.order_by(
                sort_column.desc()
            )

        else:

            query = query.order_by(
                sort_column.asc()
            )

        students = query.offset(
            skip
        ).limit(
            limit
        ).all()

        return students

    except SQLAlchemyError:

        raise


# GET student by ID
def get_student_by_id(
    db: Session,
    student_id: int
):

    try:

        student = db.query(StudentModel).filter(
            StudentModel.id == student_id
        ).first()

        return student

    except SQLAlchemyError:

        raise


# CREATE student
def create_student(
    db: Session,
    student_data: Student
):

    try:

        existing_student = db.query(
            StudentModel
        ).filter(
            StudentModel.name == student_data.name
        ).first()

        if existing_student is not None:

            return None

        new_student = StudentModel(
            name=student_data.name,
            department=student_data.department,
            year=student_data.year
        )

        db.add(new_student)

        db.commit()

        db.refresh(new_student)

        return new_student

    except SQLAlchemyError:

        db.rollback()

        raise


# UPDATE complete student
def update_student(
    db: Session,
    student_id: int,
    updated_student: Student
):

    try:

        student = get_student_by_id(
            db,
            student_id
        )

        if student is None:

            return None

        student.name = updated_student.name
        student.department = updated_student.department
        student.year = updated_student.year

        db.commit()

        db.refresh(student)

        return student

    except SQLAlchemyError:

        db.rollback()

        raise


# PATCH student
def patch_student(
    db: Session,
    student_id: int,
    updated_data: StudentUpdate
):

    try:

        student = get_student_by_id(
            db,
            student_id
        )

        if student is None:

            return None

        if updated_data.name is not None:

            student.name = updated_data.name

        if updated_data.department is not None:

            student.department = updated_data.department

        if updated_data.year is not None:

            student.year = updated_data.year

        db.commit()

        db.refresh(student)

        return student

    except SQLAlchemyError:

        db.rollback()

        raise


# DELETE student
def delete_student(
    db: Session,
    student_id: int
):

    try:

        student = get_student_by_id(
            db,
            student_id
        )

        if student is None:

            return False

        db.delete(student)

        db.commit()

        return True

    except SQLAlchemyError:

        db.rollback()

        raise