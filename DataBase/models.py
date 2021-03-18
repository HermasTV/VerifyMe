from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True,unique=True)
    first_name = Column(String, default="")
    last_name = Column(String, default="")
    address = Column(String, default="")
    city = Column(String, default="")
    match = Column(Boolean, default=False)
    action =Column(Boolean, default=False)
