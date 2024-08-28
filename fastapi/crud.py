from sqlalchemy.orm import Session
import models, schemas

# Author CRUD operations
def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Author).offset(skip).limit(limit).all()

# Book CRUD operations
def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(title=book.title, author_id=book.author_id, publisher_id=book.publisher_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_books_with_publishers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).join(models.Publisher).offset(skip).limit(limit).all()

# Publisher CRUD operations
def create_publisher(db: Session, publisher: schemas.PublisherCreate):
    db_publisher = models.Publisher(name=publisher.name)
    db.add(db_publisher)
    db.commit()
    db.refresh(db_publisher)
    return db_publisher

def get_publisher(db: Session, publisher_id: int):
    return db.query(models.Publisher).filter(models.Publisher.id == publisher_id).first()

def get_publishers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Publisher).offset(skip).limit(limit).all()
