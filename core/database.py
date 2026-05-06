from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from core.config import DATABASE_URL

DB_URL = DATABASE_URL

#engine
engine = create_engine(DB_URL,echo=True)

#factory
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

class Base(DeclarativeBase):
    pass