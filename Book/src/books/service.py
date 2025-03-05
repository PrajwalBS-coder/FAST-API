from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select,desc
from src.books.models import Book
from schemas import Bookmodel,BookCreateModel,BookUpdateModel

class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        books = await session.exec(statement)
        return books
    
    async def get_book(self,book_uuid:str,session:AsyncSession):
        statement = select(Book).where(Book.id == book_uuid)
        book = await session.exec(statement)
        return book if book is not None else None
    
    async def create_book(self,book_data:BookCreateModel,session:AsyncSession):
        data = book_data.model_dump()

        new_book_data = Book(
            **data
        )

        session.add(new_book_data)
        session.commit()
        return new_book_data

    async def update_book(self,book_uid:str,updated_data :BookUpdateModel ,session: AsyncSession):
        book_to_update = self.get_book(book_uid,session)
        if book_to_update is not None:
            update_data = updated_data.model_dump()

            for k,v in update_data.items():
                setattr(book_to_update,k,v)
            await session.commit()

            return update_data
        else:
            return None
        
    async def delete_book(self,book_id:str,session:AsyncSession):
        book_to_delete=self.get_book(book_id,session)
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit()
        else:
            return None


