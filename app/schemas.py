
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

# User
class UserBase(BaseModel):
    username: str

class UserCreate(BaseModel):
    username: str
    password: str = Field(..., max_length=72)

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# File
class FileBase(BaseModel):
    filename: str
    size: int
    description: Optional[str] = None
    theme: Optional[str] = None

class FileCreate(FileBase):
    pass

class File(FileBase):
    id: int
    stored_filename: str
    upload_time: datetime
    user_id: int

    class Config:
        from_attributes = True