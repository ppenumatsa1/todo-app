from fastapi import FastAPI
from app.db.init_db import init_db
from app.routers.todo_routers import router
from fastapi.middleware.cors import CORSMiddleware
from app.core.todo_config import settings
from app.core.todo_logging import setup_logging
import logging
from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables
env_path = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=env_path / ".env")

app = FastAPI()

# Set up logging
setup_logging()
logger = logging.getLogger(__name__)


@app.on_event("startup")
def on_startup():
    init_db()
    logger.info("Database initialized")


# Set up middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API router
app.include_router(router=router, prefix=settings.API_V1_STR, tags=["todos"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API!"}
