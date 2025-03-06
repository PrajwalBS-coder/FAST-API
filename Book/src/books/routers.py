from fastapi import APIRouter, HTTPException,status,Depends 
from fastapi.responses import JSONResponse
from src.books.schemas import Bookmodel
from src.books.books_data import books
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from src.books.service import BookService


app_router = APIRouter()
book_service = BookService()

@app_router.get("/")
async def book(session:AsyncSession= Depends(get_session)):
    books = book_service.
    return books

@app_router.get("/{id}/")
async def book(id:int):
    return next((book for book in books if book.get("id") == id), "Error")

@app_router.patch("/{id}/")
async def book(id: int,data:Bookmodel) ->dict:
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

