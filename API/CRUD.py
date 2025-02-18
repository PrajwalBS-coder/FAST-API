from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app=FastAPI()


books= [
    {
      "id": 1,
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "genre": "Classic",
      "published_year": 1925,
      "ISBN": "9780743273565",
      "pages": 180,
      "language": "English",
      "publisher": "Scribner",
      "rating": 4.4
    },
    {
      "id": 2,
      "title": "To Kill a Mockingbird",
      "author": "Harper Lee",
      "genre": "Classic",
      "published_year": 1960,
      "ISBN": "9780061120084",
      "pages": 281,
      "language": "English",
      "publisher": "J.B. Lippincott & Co.",
      "rating": 4.8
    },
    {
      "id": 3,
      "title": "1984",
      "author": "George Orwell",
      "genre": "Dystopian",
      "published_year": 1949,
      "ISBN": "9780451524935",
      "pages": 328,
      "language": "English",
      "publisher": "Secker & Warburg",
      "rating": 4.6
    },
    {
      "id": 4,
      "title": "The Catcher in the Rye",
      "author": "J.D. Salinger",
      "genre": "Fiction",
      "published_year": 1951,
      "ISBN": "9780316769488",
      "pages": 214,
      "language": "English",
      "publisher": "Little, Brown and Company",
      "rating": 4.3
    },
    {
      "id": 5,
      "title": "The Hobbit",
      "author": "J.R.R. Tolkien",
      "genre": "Fantasy",
      "published_year": 1937,
      "ISBN": "9780345339683",
      "pages": 310,
      "language": "English",
      "publisher": "George Allen & Unwin",
      "rating": 4.7
    }
  ]


@app.get("/books/")
async def book():
    return books

@app.get("/books/{id}/")
async def book(id:int):
    return next((book for book in books if book.get("id") == id), "Error")

    


class bookmodel(BaseModel):
  name :str
  author : str

@app.patch("/books/{id}/")
async def book(id: int,data:bookmodel) ->dict:
  for book in books:
    if book["id"] == id:
      book["title"]= data.name
      book["author"] = data.author
      return book
  
  raise HTTPException(detail="Not Possible",status_code=status.HTTP_400_BAD_REQUEST)
