from sqlalchemy.orm import sessionmaker, Session
from core.db import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()