from fastapi import FastAPI
# from books.routers import app_router
from src.books.routers import app_router
from contextlib import asynccontextmanager
from src.db.main import init_db



@asynccontextmanager
async def life_span(app:FastAPI):
    print("Server is starting")
    await init_db()
    yield 
    print("Server is shutting down")



app= FastAPI(
    title="Books API",
    description="A simple API that manages books",
    version="0.1",
    lifespan = life_span
    )



app.include_router(app_router ,prefix="/books",tags=["books"])