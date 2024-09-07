from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)  # Unique ID for each book
    title = Column(String, index=True)  # Book title
    author = Column(String)  # Book author
    genre = Column(String)  # Book genre
    description = Column(String, nullable=True)  # Book description 
