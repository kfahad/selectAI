from pydantic import BaseModel

# Author schemas
class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True

# Book schemas
class BookBase(BaseModel):
    title: str
    author_id: int
    publisher_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class BookWithPublisher(Book):
    publisher: str

    class Config:
        orm_mode = True

# Publisher schemas
class PublisherBase(BaseModel):
    name: str

class PublisherCreate(PublisherBase):
    pass

class Publisher(PublisherBase):
    id: int

    class Config:
        orm_mode = True
