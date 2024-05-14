from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str
    completed: bool


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
