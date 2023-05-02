from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# get database param from .env file



SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Pavel1234*@localhost:5432/python_test"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine) # session between code and db

Base = declarative_base()