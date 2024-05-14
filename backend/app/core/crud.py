from sqlalchemy.orm import Session

from . import models, schemas


def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def create_task(db: Session, item: schemas.TaskCreate):
    db_item = models.Task(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_task(db: Session, task_id: int):
    inst = db.query(models.Task).filter(models.Task.id == task_id).first()
    db.delete(inst)
    db.commit()
    return {'success': True}

# def update_task(db: Session, task_id: int, item: schemas.TaskCreate):
    # instance = db.query(models.Task).filter(
    #     models.Task.id == task_id
    # ).first()
#     for i in item:
#         setattr(instance, i.)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
