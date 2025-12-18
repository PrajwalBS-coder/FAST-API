from fastapi import APIRouter, HTTPException,status,Depends 
from fastapi.responses import JSONResponse
from src.books.schemas import Bookmodel
from src.books.books_data import books
from sqlmodel.ext.asyncio.session import AsyncSession
# src/books/routers.py
from src.db.main import get_session

from src.books.service import BookService
from src.books.schemas import Bookmodel,BookUpdateModel


app_router = APIRouter()
book_service = BookService()

@app_router.get("/")
async def book(session:AsyncSession= Depends(get_session)):
    books = book_service.get_all_books(session)#3:02
    return books


@app_router.post("/",status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Bookmodel,session:AsyncSession= Depends(get_session)) -> dict:
  new_book = book_service.create_book(book_data,session)
  return new_book


@app_router.get("/{id}/")
async def book(id:int,book:BookUpdateModel,session:AsyncSession= Depends(get_session)) ->dict:
    book =book_service.get_book(id,session)
    if book:return book
    else:
        raise HTTPException(detail="Not Possible",status_code=status.HTTP_400_BAD_REQUEST)
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

