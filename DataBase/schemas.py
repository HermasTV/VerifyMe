from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):

    token: str
    username:str
    email: str
    id: int
    first_name:Optional[str]=""
    last_name:Optional[str]=""
    address: Optional[str]=""
    match: Optional[bool] = False
    smile: Optional[bool] = False

    class Config:
        orm_mode = True


# class UserBase(BaseModel):
#     username:str
#     email: str


# class UserCreate(UserBase):
#     token: str


# class User(UserBase):
#     id: int
#     first_name:str
#     last_name:str
#     address:str
#     match:bool
#     smile: bool

#     class Config:
#         orm_mode = True

