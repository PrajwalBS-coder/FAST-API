from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from src.books.models import Book

class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book)
        books = await session.exec(statement)
        return books
    async def get(self,book:str,session:AsyncSession):
        statement = select(Book).where(Book.id == book)
        book = await session.exec(statement)
        return book