from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from src.books.models import Book
from schemas import Bookmodel,BookCreateModel,BookUpdateModel

class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book)
        books = await session.exec(statement)
        return books
    async def get(self,book:str,session:AsyncSession):
        statement = select(Book).where(Book.id == book)
        book = await session.exec(statement)
        return book

    async def update_book(self,book_uid:str,updated_data :BookUpdateModel ,session: AsyncSession):
        statement = select(Book)
        books = await session.exec(statement)
        return books