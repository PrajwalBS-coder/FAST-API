from typing import Union
from fastapi import FastAPI,Header,status
from typing import Optional
from pydantic import BaseModel
from fastapi.exceptions import HTTPException


app= FastAPI()


class  BookCreateModel(BaseModel):
    title: str
    author: str

@app.get("/")
def read_root():
    return {"Hello": "Hello World"}

@app.get("/greet/")
async def greet(name: Optional[str]="Amin",age:Optional[int]=30):
    return {"message": f"Hello {name}","Age":age }

@app.post('/createbook/')
async def create_book(book: BookCreateModel):
    return{
        "title":book.title,
        "author":book.author
    }

@app.get('/get-headers/')
def get_headers(accept: str = Header(None), x_token: str = Header(None),connection: str = Header(None), host : str = Header(None)):
    return {"Accept": accept, "X-Token": x_token,"Connection":connection , "Host":host}
