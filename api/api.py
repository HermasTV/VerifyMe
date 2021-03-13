from fastapi import FastAPI,Form,File,UploadFile

import uvicorn
import numpy as np
from cv2 import cv2
from OCR.ocr import OCR
from FaceMatch.match import Matcher
from ActionRecognition.smile import Smile

#initialize fastapi instance 
app = FastAPI()
#initialize core models
ocr = OCR()
matcher = Matcher()
smile = Smile()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/generate")
async def generate():

    pass

@app.post("/upload_id")
async def uploadID():

    pass

@app.post("/ocr")
async def id_ocr(id: UploadFile = File(...)):
    #load the Image
    contents = await id.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #img_dimensions = str(img.shape)

    #pass pass to the OCR module
    result = ocr.recognize(img)
    print(result)
    return result

@app.post("/match")
async def match(id: UploadFile = File(...),selfie: UploadFile = File(...)):

    id_data = await id.read()
    selfie_data = await selfie.read()

    id_arr = np.fromstring(id_data, np.uint8)
    selfie_arr = np.fromstring(selfie_data, np.uint8)

    id_img = cv2.imdecode(id_arr, cv2.IMREAD_COLOR)
    selfie_img = cv2.imdecode(selfie_arr, cv2.IMREAD_COLOR)

    result = matcher.match(id_card=id_img,selfie=selfie_img)[0]
    print(result)
    if result :
        result = "Matched"
    else : 
        result = "Not Matched"

    return {'result' : result}

@app.post("/action")
async def action(img: UploadFile = File(...)):
    img_data = await img.read()
    img_arr = np.fromstring(img_data, np.uint8)
    imgcv = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

    result = smile.detector(image=imgcv)

    if result :
        result = "Smile Detected"
    else : 
        result = "No smile or no Face"

    return {'result' : result}


if __name__ == '__main__':

    uvicorn.run("api:app", host='0.0.0.0', port=8000)