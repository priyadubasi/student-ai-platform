from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Student(Base):

    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    department = Column(
        String,
        nullable=False
    )

    year = Column(
        Integer,
        nullable=False
    )