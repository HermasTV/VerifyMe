import uvicorn
import secrets
import numpy as np
import pandas as pd
from cv2 import cv2
from traceback import print_exc
from typing import List,Optional

from fastapi import FastAPI,Form,File,UploadFile,Depends,HTTPException
from sqlalchemy.orm import Session
from utils.errors import *
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

# database loading
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
    return {"message": "Welcome to VerifyMe"}

@app.post("/generate")
async def generate(username:str = Form(...),
                email:str = Form(...),
                connectDB:bool = Form(...),
                db: Session = Depends(get_db)):

    token = secrets.token_urlsafe(10)
    print(connectDB)
    if connectDB:
        crud.create_user(db=db,username=username,email=email,token=token)
    return {'token':token}

@app.get("/users",response_model=List[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    
    return crud.get_users(db=db) 

@app.get("/userToken",response_model=schemas.User)
async def get_user_by_token(token:str,db: Session = Depends(get_db)):
    
    return crud.get_user_by_token(db=db,token=token)

@app.post("/ocr")
async def id_ocr(token:str = Form(...),
                id: UploadFile = File(...),
                db: Session = Depends(get_db),
                connectDB:bool = False):

    #load the Image
    contents = await id.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #pass pass to the OCR module
    try :
        result = ocr.recognize(img)

    except Exception as e :
        err = int(str(e))
        raise HTTPException(
            status_code=err,
            detail=errors[err])
        
    if connectDB: 
        crud.update_ocr(db=db,token=token,
                        first_name=result['name'],
                        last_name=result['family_name'],
                        address=result['address_line_one'],
                        city=result['address_line_two'])

    return result

@app.post("/match")
async def match(token:str= Form(...),id: UploadFile = File(...),
                selfie: UploadFile = File(...),connectDB:bool = Form(...),
                db: Session = Depends(get_db)):
    try :
        #load images 
        id_data = await id.read()
        selfie_data = await selfie.read()
        #conver them as arrays 
        id_arr = np.fromstring(id_data, np.uint8)
        selfie_arr = np.fromstring(selfie_data, np.uint8)
        #convert images to cv BGR images 
        id_img = cv2.imdecode(id_arr, cv2.IMREAD_COLOR)
        selfie_img = cv2.imdecode(selfie_arr, cv2.IMREAD_COLOR)
        #pass the images to mach module
        result = matcher.match(id_card=id_img,selfie=selfie_img)
    #one of the pre difined errors happened 
    except ValueError as v :
        err = int(str(v))
        raise HTTPException(
            status_code=err,
            detail=errors[err])
    #general exception
    except Exception as e :
        err = int(str(e))
        raise HTTPException(
            status_code=err,
            detail="General System Error")
    
    if connectDB:
        crud.update_match(db=db,token=token,match=result)

    return str(result)

@app.post("/action")
async def action(token:str = Form(...),
                 img: UploadFile = File(...),
                 connectDB:bool = Form(...),
                 db: Session = Depends(get_db)):

    img_data = await img.read()
    img_arr = np.fromstring(img_data, np.uint8)
    imgcv = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    try :
        result = smile.detector(image=imgcv)
    except ValueError as v :
        err = int(str(v))
        raise HTTPException(
            status_code=err,
            detail=errors[err])
    except Exception as e :
        print_exc()
        raise HTTPException(
            status_code=e,
            detail="General System Error")

    if connectDB:
        crud.update_action(db=db,token=token,action=result)
    return result


if __name__ == '__main__':

    uvicorn.run("api:app", host='0.0.0.0', port=8000)