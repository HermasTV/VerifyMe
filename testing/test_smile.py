import requests
from testutils import logresult

@logresult
def test_action_with_smile():
    actionPath = 'files/smile.jpg'
    token ='test_token'

    data = {'token':token,'connectDB':False}
    files = {"img": open(actionPath,'rb')}

    res = requests.post(f"http://localhost:8000/action",data=data,files=files)
    if res.status_code ==200:
        return True
    else : 
        return False

@logresult
def test_action_with_no_smile():
    actionPath = 'files/noSmile.jpg'
    token ='test_token'

    data = {'token':token,'connectDB':False}
    files = {"img": open(actionPath,'rb')}

    res = requests.post(f"http://localhost:8000/action",data=data,files=files)
    if res.status_code ==231:
        return True
    else : 
        return False

@logresult
def test_action_with_no_face():
    actionPath = 'files/uol.jpg'
    token ='test_token'

    data = {'token':token,'connectDB':False}
    files = {"img": open(actionPath,'rb')}

    res = requests.post(f"http://localhost:8000/action",data=data,files=files)
    if res.status_code ==232:
        return True
    else : 
        return False

@logresult
def test_action_with_multiple_faces():
    actionPath = 'files/group-selfie.jpg'
    token ='test_token'

    data = {'token':token,'connectDB':False}
    files = {"img": open(actionPath,'rb')}

    res = requests.post(f"http://localhost:8000/action",data=data,files=files)
    if res.status_code ==233:
        return True
    else : 
        return False


test_action_with_smile()
test_action_with_no_smile()
test_action_with_no_face()
test_action_with_multiple_faces()