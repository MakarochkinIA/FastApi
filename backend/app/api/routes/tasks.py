from fastapi import Depends, APIRouter, HTTPException
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
    if not task:
        raise HTTPException(status_code=404, detail="Item not found")
    return task


@router.delete("/{id}")
def delete_task(id: int, db: Session = Depends(get_db)):
    inst = crud.get_task(db, task_id=id)
    if not inst:
        raise HTTPException(status_code=404, detail="Item not found")
    return crud.delete_task(db, task_id=id)


def upd(
    id: int, item: schemas.TaskUpdate, db: Session = Depends(get_db)
):
    inst = crud.get_task(db, task_id=id)
    if not inst:
        raise HTTPException(status_code=404, detail="Item not found")
    d = item.model_dump(exclude_unset=True)
    for i in d.keys():
        setattr(inst, i, d[i])
    db.commit()
    db.refresh(inst)
    return inst


@router.patch("/{id}", response_model=schemas.Task)
def patch_task(
    id: int, item: schemas.TaskUpdate, db: Session = Depends(get_db)
):
    return upd(
        id, item, db
    )


@router.put("/{id}", response_model=schemas.Task)
def update_task(
    id: int, item: schemas.TaskUpdate, db: Session = Depends(get_db)
):
    return upd(
        id, item, db
    )
