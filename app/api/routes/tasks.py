from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from ..deps import get_db
from ...core import crud, schemas

router = APIRouter()


@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, item=task)


@router.get("/", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks


@router.get("/{id}", response_model=schemas.Task)
def read_task(id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id=id)
    return task


@router.delete("/{id}")
def delete_task(id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id=id)
