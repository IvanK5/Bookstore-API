from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    description: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True
