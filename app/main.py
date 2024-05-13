from fastapi import FastAPI
from .core import models, db
from .api.routes import tasks

models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()

app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
