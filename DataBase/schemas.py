from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    token: str

class UserCreate(UserBase):
    username:str
    email: str
    class Config:
        orm_mode = True

class UpdateAction(UserBase):
    action: bool
    class Config:
        orm_mode = True

class UpdateMatch(BaseModel):
    match:bool
    class Config:
        orm_mode = True

class UpdateOCR(UserBase):
    first_name:str
    last_name:str
    address:str
    city:str
    class Config:
        orm_mode = True

class User(UserCreate):
    
    first_name:str
    last_name:str
    address:str
    city:str
    match:bool
    action: bool

    class Config:
        orm_mode = True

