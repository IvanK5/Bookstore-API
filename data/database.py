from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base  # Import Base from your models.py file


SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables
Base.metadata.create_all(bind=engine)
