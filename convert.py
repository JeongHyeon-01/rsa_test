from datetime import datetime, timedelta
from fastapi import FastAPI,Response,Cookie, Request
from typing import Optional
from Crypto import Random 
from Crypto.PublicKey import RSA
from pydantic import BaseModel
from jose import jwt


public = "-----BEGIN PUBLIC KEY-----\012MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAr1Gx6qo5tON81ZygV8zn\012y3YphjIjd3GFuGBK4Ge3UGgihgezKL7348VVsvG0GY1iqE/FYhK7viyU1ZFonZ7N\012N5Rq6ZloPWFa8N5IM1cf7WL/tX8agog+RoSmAjQlRVThQWp6swOS/E4HZ6+pQoJC\012UoICybErsa0v4SqEgDxkWqBEkdihbkFMne6p0cEDdqZlBH8D6GICopJea16RWoSZ\012sqSkx+5fOaxNbrlEAsNPZEDr7Lba14FhoIODf/rPXljfI4LVh2gbnETYRec6rWCB\012gtEDyNDbkNCcEErkt7E6j32mSH2O/gJRRWV4bJuqiNyfpoZXsZvA8SdYs/6GJDpS\012RwIDAQAB\012-----END PUBLIC KEY-----"
text = b'{\n\t"domain":"Default",\n\t"password":"Admin123!",\n\t"region":"RegionOne",\n\t"username":"admin"\n}'

res = RSA.importKey(public)
cipherText = res.encrypt(text,10)
print("\n")
print("암호문 :")
print(cipherText)
