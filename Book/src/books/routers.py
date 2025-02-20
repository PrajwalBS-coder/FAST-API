from fastapi import APIRouter, HTTPException,status
from fastapi.responses import JSONResponse
from books.schemas import bookmodel
from books.books_data import books

app_router = APIRouter()



@app_router.get("/")
async def book():
    return books

@app_router.get("/{id}/")
async def book(id:int):
    return next((book for book in books if book.get("id") == id), "Error")

@app_router.patch("/{id}/")
async def book(id: int,data:bookmodel) ->dict:
  for book in books:
    if book["id"] == id:
      book["title"]= data.name
      book["author"] = data.author
      return book
  
  raise HTTPException(detail="Not Possible",status_code=status.HTTP_400_BAD_REQUEST)

@app_router.delete("/{id}/")
async def book(id : int) -> list:
  for book in books:
    if book["id"] == id:
      books.remove(book)
    return books
  else:
    raise HTTPException(detail="Not Possible",status_code=status.HTTP_400_BAD_REQUEST)

