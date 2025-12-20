from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional

app= FastAPI()

items=[]

#Creating a pydantic model
"""
Here name field is a required field and min_length and max_length are constraints
And price field is optional and gt and lt are constraints
"""
class Item(BaseModel):
    name:  str = Field(...,min_length=3,max_length=10)
    price: Optional[float] = Field(None,gt=0,lt=100)

@app.get("/get/")
async def root():
    return {"message": "Hello World"}

@app.post("/add/")
async def add_item(item: Item):
    items.append(item)
    return item


@app.get("/get_all/")
async def get_item():
    return items