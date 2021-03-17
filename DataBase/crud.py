from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_token(db: Session, token: str):
    return db.query(models.User).filter(models.User.token == token).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def update_match(db: Session, token: str ,match:bool):
    user = get_user_by_token(db,token)
    user.match = match
    todo.completed = todo.completed
    db.commit()
    db.refresh(todo)
    return todo

def update_ocr(db: Session, token: str,first_name:str,last_name:str,address:str):
    pass
def update_action(db: Session, token: str ,action:bool):
    pass

def create_user(db: Session,username:str , email:str ,token:str):
    
    db_user = models.User(username = username, email=email,token=token)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
