from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# Payload and validation
class Note(BaseModel):
    title: str
    content: str    
    published: bool
    # using serializer
    class Config:
        orm_mode = True

class CreateNote(BaseModel):
    title: str
    content: str
    # using serializer
    class Config:
        orm_mode = True

class UpdateNote(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: bool = True

