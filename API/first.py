from typing import Union
from fastapi import FastAPI
from typing import Optional

app= FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Hello World"}

@app.get("/greet/")
async def greet(name: Optional[str]="Amin",age:Optional[int]=30):
    return {"message": f"Hello {name}","Age":age }