import requests
from testutils import logresult

@logresult
def test_match_face_matched():
    facePath = 'files/selfie.jpg'
    idPath = 'files/id.jpg'
    token = 'test_token'

    data = {'token':token,'connectDB':False}
    files = {"id": open(idPath,'rb'),
            "selfie":open(facePath,'rb')}

    res = requests.post(f"http://localhost:8000/match",data=data, files=files)

    print(res.status_code)
    if res.status_code == 200:
        return True
    else :
        return False
    

    
@logresult
def test_match_face_not_matched():
    facePath = 'files/obama.jpg'
    idPath = 'files/id.jpg'
    token = 'test_token'

    data = {'token':token,'connectDB':False}
    files = {"id": open(idPath,'rb'),
            "selfie":open(facePath,'rb')}

    res = requests.post(f"http://localhost:8000/match",data=data, files=files)
    if res.status_code == 221:
        return True
    else :
        return False 

@logresult
def test_match_no_face():
    facePath = 'files/uol.jpg'
    idPath = 'files/id.jpg'
    token = 'test_token'

    data = {'token':token,'connectDB':False}
    files = {"id": open(idPath,'rb'),
            "selfie":open(facePath,'rb')}

    res = requests.post(f"http://localhost:8000/match",data=data, files=files)
    if res.status_code == 222:
        return True
    else : 
        return False 

@logresult
def test_match_multiple_faces():
    facePath = 'files/group-selfie.jpg'
    idPath = 'files/id.jpg'
    token = 'test_token'

    data = {'token':token,'connectDB':False}
    files = {"id": open(idPath,'rb'),
            "selfie":open(facePath,'rb')}

    res = requests.post(f"http://localhost:8000/match",data=data, files=files)
    if res.status_code == 223:
        return True
    else : 
        return False  

# test_match_face_matched()
# test_match_face_not_matched()
# test_match_no_face()
# test_match_multiple_faces()