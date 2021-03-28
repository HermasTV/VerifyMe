import requests
from testutils import logresult

@logresult
def test_ocr_with_id():
    imgPath = 'files/id.jpeg'
    token ='test_token'

    data = {'token':token,'connectDB':False}
    files = {"id": open(imgPath,'rb')}

    res = requests.post(f"http://localhost:8000/ocr",data=data,files=files)
    if res :
        return True
    else : 
        return False

@logresult
def test_ocr_with_no_id():
    imgPath = 'files/noid.jpg'
    token ='test_token'

    data = {'token':token,'connectDB':False}
    files = {"id": open(imgPath,'rb')}
    
    res = requests.post(f"http://localhost:8000/ocr",data=data,files=files)

    if res.status_code == 201:
        return True
    else :
        return False

@logresult
def test_ocr_with_missing_fields():
    imgPath = 'files/missing.jpeg'
    token ='test_token'

    data = {'token':token,'connectDB':False}
    files = {"id": open(imgPath,'rb')}
    
    res = requests.post(f"http://localhost:8000/ocr",data=data,files=files)
    if res.status_code ==202:
        return True
    else :
        return False
        
#test_ocr_with_id()
test_ocr_with_no_id()
test_ocr_with_missing_fields()