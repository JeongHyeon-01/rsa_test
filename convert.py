from datetime import datetime, timedelta
from fastapi import FastAPI,Response,Cookie, Request
from typing import Optional
from Crypto import Random 
from pydantic import BaseModel
from jose import jwt
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

private = '''-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAguLURwwOR6nNVaGq1PsM1LNjWfGTTaPwWQdIeaKWC4AlmkM4
FqriVPCQLqRVT7sE41zOoMPHD07h9Vst70FSxxwfBXBXwLl71EiowSqd7mITS0GU
oqyXahlzbPLkmnw9o8wn/L9Os/wspOeaYaVqOXBBCv8U6W7GZoTJvvdIXdb2hved
2XPl7n/SOulrB12KCnxCNPypcm1JxQQjhvUwIxs0rdmrIKE14qjuYzg0RIXAU4/D
3RfTFJBWW7uiZx2ikzvQJII2+kowJcNATM5IET519DBf8IPlUWf/UaGQxLglxou3
HEJFoSyrRDOXvsAodmu8AazIQd6PiDMXrCWP0QIDAQABAoIBAFYbOgIfmUlmGVLr
j8KcAr3v4j2q4viiEJ3RX8m9v66DOLm63Sx0cX/l30UAEavpYnbdeIZlJhEZGShc
OuT6+aVKB9KBLQn6PM/UmUiza8EHPqA03b8Dgn1njvsu9Fv5vmeDCQ+LIBDiptA6
GeOBeledVP0SAUTs/pM1arA6aJ5qu11gjvPE64/PStMJA2fbcIVI2tP+bY8C651i
1OgJOl5Npb/QWPbRH0IttWArX+9pET5g3ehf3eTNsEetb/RmUqg1zc+7Q15WXsC7
swnPFE79m5FjCpeHYqDVRxYodYCGu0A/McSvMIgit01pOVEd3Evk8B4uXHn/3Af3
3l9EhlECgYEAt2lhwP5Sy1JLdcueYiGMixhiBsii4XhZTTd9bAage1IfubS8p4k/
Yh6xVEmUXmkdJd6w3BUMNeyMqc4cPUDqhnHFqVnDcrBMU3D0HRYjzJAIENZ6n/vo
eERlQhM/KkOWu8Duy5SP7Ms05Rkn+5t/VW4sjJSvmnIMLLLBvqNfXS0CgYEAtq+9
dvDfo8zbsOUw9EPqodoBY3SbwCqS2IQC9B5/AOFAVSLLdli1zWePdX1Ve2kmtDGD
iq2kZJWwvjKWwhFc6QpU8T5R/r9F2WL03dFT/RSsadw4b8zieXcOlE0hUf76DJNy
qv0troaD563jqc3W9E7a//pD/i8hXK1vjXfuy7UCgYEAjD5IQQo2xMFoceoAcYi1
rqY2TnmcEkuz/RcxECkBDUr+d0F7/58ymBRgA9M/X/GAGDTvh1mQvKrj4/N2JGA+
9A6K1bONf2TO9/6mqpcDSKfZgwZ9PVehqlSiGKQe6HJGD8q2zXQLmUTIbWWO7RU5
iFl2Nwh6Pd528La+7sZ9ZQECgYEAigtODbyCIZJBR/BIB6vydo73kaGht5n0EKvg
V3tb2Nxc8ngyaqEp76abntowZ+rTFkJ79aS0nlUGkxJDHS5lmKr3+Ltw1iDOtS+z
fJIa9xhSGEQSWVjmoYY3fBS0YvNbG3mnolFh3YlDzyN07vDdxwp3Lgp8qmwOt6tO
qgXAaikCgYBp0R85F8qaWg1RR3DH3ke3l++vZyqYNJcWE7L2/x2KmAdcb3hy4m7P
oqIlot2LQE1aYao+F5KYnriPhUcu5EJAONELFo24/c/8D4p/0oP1ubgKrYnm039j
9m98tV/WwKo3h+PdugDSJNHNBCVBOUDQa/1kGYNI8WLE3DntzYCAcg==
-----END RSA PRIVATE KEY-----
'''
public ='''
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAguLURwwOR6nNVaGq1PsM
1LNjWfGTTaPwWQdIeaKWC4AlmkM4FqriVPCQLqRVT7sE41zOoMPHD07h9Vst70FS
xxwfBXBXwLl71EiowSqd7mITS0GUoqyXahlzbPLkmnw9o8wn/L9Os/wspOeaYaVq
OXBBCv8U6W7GZoTJvvdIXdb2hved2XPl7n/SOulrB12KCnxCNPypcm1JxQQjhvUw
Ixs0rdmrIKE14qjuYzg0RIXAU4/D3RfTFJBWW7uiZx2ikzvQJII2+kowJcNATM5I
ET519DBf8IPlUWf/UaGQxLglxou3HEJFoSyrRDOXvsAodmu8AazIQd6PiDMXrCWP
0QIDAQAB
-----END PUBLIC KEY-----'''

# public =b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8krG4qYko3rvzdaM+BnOaCSjm\nO6q22ou8E+HYhxjHC6RcthHHOJacbsWo9cBX0pnM31YOUp53KBO07RlV5SnjQeF2\nXtNl8dOYtkCPPTz7up5xnzIFiQgNTRH0AsXs4HTL6vxG9bvCf7ezcK5vOhSfOdS9\nDQ1/9MMo4xnrqpehcQIDAQAB\n-----END PUBLIC KEY-----'
# text = b'{\n\t"domain":"Default",\n\t"password":"Admin123!",\n\t"region":"RegionOne",\n\t"username":"admin"\n}'
# res = RSA.import_key(public)
# session_key = get_random_bytes(16)
# cipher_rsa = PKCS1_OAEP.new(res)
# enc_session_key = cipher_rsa.encrypt(session_key)
# cipher_aes = AES.new(session_key, AES.MODE_EAX)
# ciphertext = cipher_aes.encrypt(text)

# cipherText = (b'\x1bS\xbex\xe3:\x9c\x0f\xce\xd1\r\xec\x1d\xe6\x075\x8b\xcd\x9aP0\x0bk\x05w\xf1e,%\xe6\xb96\x06\xe7+\xae\x17>\xfe\xa4\x8b$\xbb\x18\\\x83\x9b\xb4j8\'"\xb4\'\xfa\xe2\xe3Q9+s\xeb\x082\xd3\x1aT\xf3b5\xd8\x82\xe3\xe7\x11\xbc\r\x89\xef{\xf9\x98\xe7\xe5\x9d\xd3\x0c\x1c]eQ\x80\x81z8\xa5\xe3\xc9\xb6\xa5Lc\x1ab\xb1\xb2\x0c\xf4\x8d5,Am\xde\xbc\xdb\rTri#\xed\xcf\xbb\x9a\x7fu\xd5];\xcf1\xad6\x92\x96\x87\xd1\xd4dSC-PCM\xb6\xa1\xdc!o\x8b\xdc\x80\x1e\xf3\xa1p\xccL\x9f\x1d0hq\xce"\xd1C\x91\x93s\xbe\xbe\xbb\x00\x90\x02\x81\xf6\xf7T\xc3\xba2\x01\xb7WF\xd5rNe!\xda\xf4\xd0\x9d4\xbc\xd8\xc7\xa7n\xbaT\x07I @\xa3\xec\xe8c<\xe5\xfar\xba>\xf6Iy\xf4$\xb9M[\xbbao\xf2\xa1#N\xb9^\xb7\x96\xd1M\x95G@i\xe9#\x97h\xd4M-\x92]\xd2\xbe',)
# print("\n")
# print("????????? :")
# print(ciphertext, "\n", type(ciphertext))

### in <module>
    decryptor = PKCS1_OAEP.new(privKey)ipher_rsa.decrypt(ciphertext)

#decryption
# key = RSA.importKey(private)
# res = key.decrypt(cipherText).decode()
print("\n")
print("Plan Text :")
print(eval(res), "\n", type(eval(res)))