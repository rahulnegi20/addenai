from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from core.models import Base
from sqlalchemy.orm import sessionmaker, Session


URL_DATABASE = "postgresql://postgres:insert2021@localhost:5432/advert"

engine = create_engine(URL_DATABASE)

SessionLocal =sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)