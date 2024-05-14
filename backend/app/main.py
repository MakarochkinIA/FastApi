from fastapi import FastAPI

from .api.routes import tasks
from .core import models, db
models.Base.metadata.create_all(bind=db.engine)

app = FastAPI()

app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])
