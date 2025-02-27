from pydantic import BaseModel
import uuid
from datetime import datetime 
class Bookmodel(BaseModel):
  uid : uuid.UUID
  title : str
  name :str
  author : str
  publisher : str
  date : str
  pages : int
  language : str
  created_at : datetime
  updated_at : datetime#2:37:54

class BookCreateModel(BaseModel):
  title : str
  name :str
  author : str
  publisher : str
  date : str
  language : str


class BookUpdateModel(BaseModel):
  title : str
  name :str
  author : str
  publisher : str
  date : str
  language : str