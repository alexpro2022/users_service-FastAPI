from fastapi import FastAPI

from app.api import main_router
from app.core import settings

app = FastAPI(title=settings.app_title, description=settings.app_description)

app.include_router(main_router)
