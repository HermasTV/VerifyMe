from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class MyDB():
    def __init__(self):
        pass

DB_URL = "sqlite:///./DataBase.db"
#DB_URL = "postgresql://verifyme:verifyme@127.0.0.1:5432/testdb"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
