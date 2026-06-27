from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)
