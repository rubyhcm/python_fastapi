from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr

# Payload and validation
class UserOut(BaseModel):
    id: UUID
    email: str
    class Config:
        from_attributes = True

class Note(BaseModel):
    id: UUID
    title: str
    content: str    
    published: bool
    user: UserOut
    # using serializer
    class Config:
        from_attributes = True

class CreateNote(BaseModel):
    title: str
    content: str
    # using serializer
    class Config:
        from_attributes = True

class UpdateNote(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: bool = True

class UserCreate(BaseModel):
    # validate email
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str]

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
