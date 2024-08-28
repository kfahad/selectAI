from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import * 
from crud import * 
from schemas import *

# Create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD operations for Author
@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)

@app.get("/authors/", response_model=list[schemas.Author])
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    authors = crud.get_authors(db, skip=skip, limit=limit)
    return authors

@app.get("/authors/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author

# CRUD operations for Book
@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# CRUD operations for Publisher
@app.post("/publishers/", response_model=schemas.Publisher)
def create_publisher(publisher: schemas.PublisherCreate, db: Session = Depends(get_db)):
    return crud.create_publisher(db=db, publisher=publisher)

@app.get("/publishers/", response_model=list[schemas.Publisher])
def read_publishers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    publishers = crud.get_publishers(db, skip=skip, limit=limit)
    return publishers

@app.get("/publishers/{publisher_id}", response_model=schemas.Publisher)
def read_publisher(publisher_id: int, db: Session = Depends(get_db)):
    db_publisher = crud.get_publisher(db, publisher_id=publisher_id)
    if db_publisher is None:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return db_publisher

# Example of a JOIN query
@app.get("/books/with-publishers/", response_model=list[schemas.BookWithPublisher])
def read_books_with_publishers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books_with_publishers = crud.get_books_with_publishers(db, skip=skip, limit=limit)
    return books_with_publishers
