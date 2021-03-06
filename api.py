from fastapi import FastAPI,Form,File,UploadFile

import uvicorn
import numpy as np
from cv2 import cv2
from OCR.ocr import OCR

app = FastAPI()
ocr = OCR()




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
async def match():
    
    pass

@app.post("/action")
async def action():
    pass


# if __name__ == '__main__':

#     uvicorn.run(app, host='127.0.0.1', port=8000)