from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Get the database URL from .env, default to SQLite if not found
# This allows us to switch between SQLite (local) and Postgres (Docker) easily
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./news.db")

# Create the database engine
# connect_args={"check_same_thread": False} is needed only for SQLite
connect_args = {"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args=connect_args
)

# Create a SessionLocal class
# Each time we need to talk to the DB, we create an instance of this
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
