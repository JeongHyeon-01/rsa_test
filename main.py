
from fastapi import FastAPI,Response,Cookie
from typing import Optional
from Crypto import Random 
from Crypto.PublicKey import RSA
from pydantic import BaseModel


random_generator = Random.new().read

app = FastAPI()
keyPair = RSA.generate(2048,random_generator)
  

class Text(BaseModel):
    content : str

@app.get("/")
async def root():
    return {"message" : "hello"}

@app.get("/psm")
async def auth(response: Response):
    privKey = keyPair.exportKey('PEM') #이부분 한번 더 감쌀수있는 게 필요함
    public_key = keyPair.publickey().exportKey("PEM")
    # print(public_key.implementation)
    response.set_cookie(key="privKey", value = privKey.decode('utf-8')) 
    response.set_cookie(key="public", value = public_key.decode('utf-8'))
    return  public_key

@app.post("/convert")
async def convert(
    response: Response,\
    content : Text, \
    privKey : Optional[str] = Cookie(None),\
    public : Optional[str] = Cookie(None)
        ):

    #암호화
    public = public.encode('utf-8')
    res = RSA.importKey(public)
    cipherText = res.encrypt(str(content).encode(),10)
    print("\n")
    print("암호문 :")
    print(cipherText)

    #복호화
    print('\n')
    private = privKey.encode('utf-8')
    key = RSA.importKey(private)
    res = key.decrypt(cipherText).decode()
    print("\n")
    print("해독문 :")
    print(res,type(res))
    response.delete_cookie("privKey")
    response.set_cookie(key="JWT", value= "JWT is in here")
    return res