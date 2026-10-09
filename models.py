import os
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine


class User(SQLModel, table=True):
    __tablename__ = 'users'

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: Optional[int] = Field(default=None)


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:1@localhost:5433/postgres")
engine = create_engine(DATABASE_URL)


def create_tables():
    SQLModel.metadata.create_all(engine)
