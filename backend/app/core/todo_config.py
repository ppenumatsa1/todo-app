from pydantic import BaseSettings
from dotenv import load_dotenv
import os
import logging

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    DATABASE_USER: str = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD")
    DATABASE_HOST: str = os.getenv("DATABASE_HOST")
    DATABASE_PORT: str = os.getenv("DATABASE_PORT")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")

    API_V1_STR: str = os.getenv("API_V1_STR")

    class Config:
        env_file = ".env"
        extra = "allow"
        env_file_encoding = "utf-8"


settings = Settings()
