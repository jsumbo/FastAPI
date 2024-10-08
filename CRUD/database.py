from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative base #type: ignore 
from sqlalchemy.orm import sessionmaker #type: ignore 

SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # type: ignore