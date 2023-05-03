from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path("sql_app/.env")
load_dotenv(dotenv_path=env_path)
# load_dotenv()

# get database param from .env file

class Settings():

    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT =   os.getenv("POSTGRES_PORT")
    POSTGRES_DB  = os.getenv("POSTGRES_DB")
    SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Pavel1234*@localhost:5432/python_test"

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine) # session between code and db

Base = declarative_base()