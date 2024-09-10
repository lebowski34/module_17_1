from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from sqlalchemy.testing.plugin.plugin_base import engines
from sqlalchemy import Column, Integer, String

engine = create_engine("sqlite:///taskmanager.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

from app.routers import user, task

Base.metadata.create_all(bind=engine)
