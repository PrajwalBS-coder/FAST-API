from pydantic import BaseModel
import uuid
from datetime import datetime 
class bookmodel(BaseModel):
  uid : uuid.UUID
  title : str
  name :str
  author : str
  publisher : str
  date : str
  pages : int
  created_at : datetime
  updated_at : datetime#2:37:54