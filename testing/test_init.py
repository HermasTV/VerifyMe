import requests
import secrets
from testutils import logresult

testname = secrets.token_urlsafe(10)
testmail = secrets.token_urlsafe(10)

@logresult
def test_init_new():
    req={
        'username':testname,
        'email': testmail,
        'connectDB':True
        }
    res = requests.post(f"http://localhost:8000/generate",data=req,)
    return res.ok

@logresult
def test_init_duplicate():
    req={
        'username':testname,
        'email': testmail,
        'connectDB':True
        }
    res = requests.post(f"http://localhost:8000/generate",data=req)
    return res.ok

@logresult
def test_init_missing_field():
    req={
        'username':testname,
        'connectDB':True}
            
    res = requests.post(f"http://localhost:8000/generate",data=req)
    return res.ok

test_init_new()
test_init_duplicate()
test_init_missing_field()