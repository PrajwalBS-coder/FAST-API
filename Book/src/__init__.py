from fastapi import FastAPI
# from books.routers import app_router
from src.books.routers import app_router
app= FastAPI(
    title="Books API",
    description="A simple API that manages books",
    version="0.1"
    )



app.include_router(app_router ,prefix="/books",tags=["books"])