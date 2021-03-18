import uvicorn
import secrets
import numpy as np
from cv2 import cv2
from typing import List,Optional

from fastapi import FastAPI,Form,File,UploadFile,Depends
from sqlalchemy.orm import Session
from modules.OCR.ocr import OCR
from modules.FaceMatch.match import Matcher
from modules.ActionRecognition.smile import Smile
#import database 
import DataBase
from DataBase import crud,models,schemas
from DataBase.database import SessionLocal,engine

models.Base.metadata.create_all(bind=engine)
#initialize fastapi instance 
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#initialize core models
ocr = OCR()
matcher = Matcher()
smile = Smile()



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/generate",response_model=schemas.UserCreate)
async def generate(username:str = Form(...),
                email:str = Form(...),
                db: Session = Depends(get_db)):

    token = secrets.token_urlsafe(10)
    return crud.create_user(db=db,username=username,email=email,token=token)

@app.get("/users",response_model=List[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    
    return crud.get_users(db=db)

@app.get("/userToken",response_model=schemas.User)
async def get_user_by_token(token:str,db: Session = Depends(get_db)):
    
    return crud.get_user_by_token(db=db,token=token)

@app.post("/ocr",response_model=schemas.User)
async def id_ocr(token:str = Form(...),
                id: UploadFile = File(...),
                db: Session = Depends(get_db)):

    #load the Image
    contents = await id.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #img_dimensions = str(img.shape)

    #pass pass to the OCR module
    result = ocr.recognize(img)
    user = crud.update_ocr(db=db,token=token,
                    first_name=result['name'],
                    last_name=result['family_name'],
                    address=result['address_line_one'],
                    city=result['address_line_two'])

    return user

@app.post("/match",response_model=schemas.UpdateMatch)
async def match(token:str= Form(...),
                id: UploadFile = File(...),
                selfie: UploadFile = File(...),
                db: Session = Depends(get_db)):

    id_data = await id.read()
    selfie_data = await selfie.read()

    id_arr = np.fromstring(id_data, np.uint8)
    selfie_arr = np.fromstring(selfie_data, np.uint8)

    id_img = cv2.imdecode(id_arr, cv2.IMREAD_COLOR)
    selfie_img = cv2.imdecode(selfie_arr, cv2.IMREAD_COLOR)

    result = matcher.match(id_card=id_img,selfie=selfie_img)[0]
    user = crud.update_match(db=db,token=token,match=result)
    return user

@app.post("/action",response_model=schemas.UpdateAction)
async def action(token:str = Form(...),
                 img: UploadFile = File(...),
                 db: Session = Depends(get_db)):

    img_data = await img.read()
    img_arr = np.fromstring(img_data, np.uint8)
    imgcv = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

    result = smile.detector(image=imgcv)

    return crud.update_action(db=db,token=token,action=result)


if __name__ == '__main__':

    uvicorn.run("api:app", host='0.0.0.0', port=8000)