from sqlalchemy import Boolean, Column, Integer, String

from .db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean)
