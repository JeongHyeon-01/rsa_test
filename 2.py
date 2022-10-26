from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(2048,random_generator)
# print("generate key : ",key)
# private_key = key.export_key()
private_key = '''-----BEGIN RSA PRIVATE KEY-----
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
# print("private key : ",private_key)

# public_key = key.publickey().export_key()

public_key ='''
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAguLURwwOR6nNVaGq1PsM
1LNjWfGTTaPwWQdIeaKWC4AlmkM4FqriVPCQLqRVT7sE41zOoMPHD07h9Vst70FS
xxwfBXBXwLl71EiowSqd7mITS0GUoqyXahlzbPLkmnw9o8wn/L9Os/wspOeaYaVq
OXBBCv8U6W7GZoTJvvdIXdb2hved2XPl7n/SOulrB12KCnxCNPypcm1JxQQjhvUw
Ixs0rdmrIKE14qjuYzg0RIXAU4/D3RfTFJBWW7uiZx2ikzvQJII2+kowJcNATM5I
ET519DBf8IPlUWf/UaGQxLglxou3HEJFoSyrRDOXvsAodmu8AazIQd6PiDMXrCWP
0QIDAQAB
-----END PUBLIC KEY-----'''

print("public_key : ",public_key)

# data = "I met aliens in UFO. Here is the map.".encode("utf-8")

recipient_key = RSA.import_key(private_key)
cipher_rsa = PKCS1_OAEP.new(recipient_key)
session_key = get_random_bytes(16)
enc_session_key = cipher_rsa.encrypt(session_key)

cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext = cipher_aes.encrypt(data)
print(ciphertext)

private_key = RSA.import_key(private_key)
print(private_key.size_in_bytes())