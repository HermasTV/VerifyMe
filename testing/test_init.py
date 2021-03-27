import requests
import secrets
from testutils import logresult

testname = secrets.token_urlsafe(10)
testmail = secrets.token_urlsafe(10)

@logresult
def test_init_new():
    req={
        'username':testname,
        'email': testmail
        }      
    res = requests.post(f"http://localhost:8000/generate",data=req)
    return res.status_code

@logresult
def test_init_duplicate():
    req={
        'username':testname,
        'email': testmail
        }
    res = requests.post(f"http://localhost:8000/generate",data=req)
    return res.status_code

@logresult
def test_init_missing_field():
    req={
        'username':testname}
            
    res = requests.post(f"http://localhost:8000/generate",data=req)
    return res.status_code
