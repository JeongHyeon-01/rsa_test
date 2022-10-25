from datetime import datetime, timedelta
from fastapi import FastAPI,Response,Cookie, Request
from typing import Optional
from Crypto import Random 
from Crypto.PublicKey import RSA
from pydantic import BaseModel
from jose import jwt



SECRET_KEY = "6f81760a303acf1f1c9709f080f42f5f05af8110393ed82e345880f858decbed"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 600

class Token(BaseModel):
    pre_token: str
    token_type: str

class Payload(BaseModel):
    keystone_token: str
    region: str
    exp: int
    uuid: str

    
class user(BaseModel):
    content : str
    username : str
    password : str


def create_access_token(data: dict, expires_delta:None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


random_generator = Random.new().read

app = FastAPI()
keyPair = RSA.generate(2048,random_generator)
  

class Creditinal(BaseModel):
    content : str
    username : str
    password : str

@app.get("/")
async def root():
    return {"message" : "hello"}

@app.get("/preincript")
async def auth(response: Response):
    privKey = keyPair.exportKey("PEM") 
    public_key = keyPair.publickey()
    # print(public_key.implementation)

    token = create_access_token(
        {
            "pritvate_Key" : privKey.decode('utf-8'),
        },
        expires_delta = timedelta(minutes=5)
    )
    
    response.set_cookie(key= "pre_token",value = token) 
    response.set_cookie(key="public", value = public_key.exportKey("PEM").decode('utf-8'))
    public = {
        "n" : public_key.n,
        "e" : public_key.e 
    }

    return  public

@app.post("/convert")
async def convert(
    response: Response,\
    request : Request,\
    pre_token : Optional[str] = Cookie(None),\
    public : Optional[str] = Cookie(None),\
        ):
    # print(pre_token, type(pre_token))
    address = request.headers.get('cookie')
    print(address)
    print("\n")
    
    #Pre_jwt 복호화
    decode_jwt = jwt.decode(pre_token,SECRET_KEY)
    print("\n")
    print("복호문 : ")
    print(decode_jwt)

    private_key = decode_jwt["pritvate_Key"]
    
    #암호화
    public = public.encode('utf-8')
    res = RSA.importKey(public)
    print(res)
    print(await request.body())
    cipherText = res.encrypt(await request.body(),10)
    print("\n")
    print("암호문 :")
    print(cipherText)

    # #복호화
    print('\n')
    # private = private_key.encode('utf-8')
    key = RSA.importKey(private_key)
    res = key.decrypt(cipherText).decode()
    print("\n")
    print("해독문 :")
    
    result = eval(res)
    print("\n")
    print(eval(res))
    
    user_token = create_access_token(
        {
            "keystone_token": "qwertyuiop",
            "region" : "test_in_local",
            "uuid" : "1234567890"
        },
        expires_delta= timedelta(minutes=5)
    )
    Creditinal.content = result["content"]
    Creditinal.username = result["username"]
    Creditinal.password = result["password"]
    
    
    response.set_cookie(key="JWT", value= user_token)
    print("\n")
    print("RESULT : Value 값만 추출")
    print(Creditinal.username, Creditinal.password, Creditinal.content )
    
    return res

