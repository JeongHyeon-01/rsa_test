from datetime import datetime, timedelta
from fastapi import FastAPI,Response,Cookie, Request
from typing import Optional
from Crypto import Random 
from Crypto.PublicKey import RSA
from pydantic import BaseModel
from jose import jwt
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP,AES
from Crypto.Random import get_random_bytes


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

@app.get(
    "/key",
    description="Get your access RSA.",
    response_description="OK",
)
async def key(response: Response):
    random_generator = Random.new().read
    keyPair = RSA.generate(2048,random_generator)
    public_key = keyPair.publickey()

    data = {
        "private" : keyPair.export_key("PEM").decode()
    }
    to_encode = data.copy()
    #30분은 임시 값입니다.
    exp = datetime.utcnow() + timedelta(days=1)
    to_encode.update({"exp": exp})
    temporary_token = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    response.set_cookie(key="temporary_token", value=temporary_token)
    #Test용 임시코드
    response.set_cookie(key="public", value=public_key.exportKey("PEM").decode('utf-8'))
    public = {
        "n" : str(public_key.n),
        "e" : public_key.e
    }

    return public
    

@app.post("/convert")
async def convert(
    response: Response,\
    request : Request,\
    temporary_token : Optional[str] = Cookie(None),\
    public : Optional[str] = Cookie(None),\
        ):
    try:
        decode_jwt = jwt.decode(temporary_token,SECRET_KEY)
        private_key = decode_jwt["private"]
        data = str(await request.body(), 'utf-8')
        print(data.split('/'))
        data = await request.body()
        
        # recipient_key = PKCS1_OAEP.new(public)
        
        # enc_session_key = cipher_rsa.encrypt(session_key)
        
        recipient_key = RSA.import_key(public)
        session_key = get_random_bytes(16)
        
        #암호화
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        print(cipher_aes)
        # # print(ciphertext)
        # # print(tag)
        a = [ x for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
        print(a[0], type(a[0]))
        print(a[1], type(a[1]))
        print(a[2], type(a[2]))
        print(a[3], type(a[3]))
        
        #복호화

        private_key = RSA.import_key(private_key.encode())
        
        enc_session_key, nonce, tag, ciphertext = [x for x in a]
        # print("enc_session_key : ",enc_session_key)
        # print("nonce : ", nonce)
        # print("ciphertext : ",ciphertext)
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt(ciphertext)
        
        # print(data.decode("utf-8"))
        # print(a)

        # print(enc_session_key)
        # cipher_rsa = PKCS1_OAEP.new(private_key)
        # session_key = cipher_rsa.decrypt(enc_session_key)
        # cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)

        
        # session_key = cipher_rsa.decrypt(await request.body())
        
        return data.decode("utf-8")
    
    except ValueError:
        return "ValueError: Ciphertext with incorrect length."
    # print(pre_token, type(pre_token))
    # address = request.headers.get('cookie')
    # print(address)
    # print("\n")
    
    # #Pre_jwt 복호화
    # decode_jwt = jwt.decode(pre_token,SECRET_KEY)
    # print("\n")
    # print("복호문 : ")
    # print(decode_jwt)

    # private_key = decode_jwt["pritvate_Key"]
    
    # #암호화
    # public = public.encode('utf-8')
    # res = RSA.importKey(public)
    # print(res)
    # print(await request.body())
    # cipherText = res.encrypt(await request.body(),10)
    # print("\n")
    # print("암호문 :")
    # print(cipherText)
    # # a = (b"\x11\xaa\x15\x93\x8fEO\xf7\xd6\xca\xde\xa3\x19<\xf5M@ \xf0\x80h\xe0\xf5K\xb7X\xf1\x02\x08L{K\x07\x11Cp\xd9\x1c\xf9\t\x03\x0e}\xa42\xae\xe2\xc9\xa7J\xc3\xd0p\xea\xdcT\xc0\xbb\x94\x98\xd9q\xf3\xdc\xd3%\xd6\xce\xfc\xe5%\xb7\xf9\xc8\xa3\x16Z\x8a\xa3y\x9b\xd3\xe3(\x9b\x05`\x86\x8e\xb1\xbd\xb90\xa2\xd6N \xa7\xc4\xd2tbLsw\x93\xb5D\xfdIDL\xd0\x1e\x9f\xdc\x16\nZ\xc8_E|\x0f\xc1\x98D\x04\x119\x8d\xcd\x12\xc4\xa0\x94%\x9e\xbd\xdb\xbd\xac%\xc9'\x99)\x1ebk~\xe3\xe5\xa8i4;\x03\xe1|\x8a<\xf1_\xfe\xac\xa0\xf4\x0c\xad}\xd3\xfb+m\xc0\xcb3\xe4d\x9a\xc2\x96\x13_k0@T\x13#\xb5\xb2\x11\x1d_9\x9a\xfbQ_\xf4\x84\x06%\xdf\xbeW_\xe4\xdb\xcd8!lgg+W\xc4GsYu\x04\x89[\x1bE\x0b\x8bK6\x0f\xf7\x9cb\x8c\x06\xb7kF3L\xa2Pj\xd7\xbda!Md\xe12p",)
    # # #복호화
    # print('\n')
    # # private = private_key.encode('utf-8')
    # key = RSA.importKey(private_key)
    # res = key.decrypt(a).decode()
    # print("\n")
    # print("해독문 :")
    
    # result = eval(res)
    # print("\n")
    # print(eval(res))
    
    # user_token = create_access_token(
    #     {
    #         "keystone_token": "qwertyuiop",
    #         "region" : "test_in_local",
    #         "uuid" : "1234567890"
    #     },
    #     expires_delta= timedelta(minutes=5)
    # )
    # Creditinal.content = result["content"]
    # Creditinal.username = result["username"]
    # Creditinal.password = result["password"]
    
    
    # response.set_cookie(key="JWT", value= user_token)
    # print("\n")
    # print("RESULT : Value 값만 추출")
    # print(Creditinal.username, Creditinal.password, Creditinal.content )
    
    # return res

