from Crypto.PublicKey import RSA
from Crypto import Random 
from Crypto.Cipher import AES, PKCS1_OAEP
# Private key와 Public key 쌍을 생성한다.
# Private key는 소유자가 보관하고, Public key는 공개한다. 


random_generator = Random.new().read

keyPair = RSA.generate(1024,random_generator)
privKey = keyPair.exportKey()
# 키 소유자 보관용
privKey = '''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''
 #keyPair.publickey()

publicKey ='''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAguLURwwOR6nNVaGq1PsM
1LNjWfGTTaPwWQdIeaKWC4AlmkM4FqriVPCQLqRVT7sE41zOoMPHD07h9Vst70FS
xxwfBXBXwLl71EiowSqd7mITS0GUoqyXahlzbPLkmnw9o8wn/L9Os/wspOeaYaVq
OXBBCv8U6W7GZoTJvvdIXdb2hved2XPl7n/SOulrB12KCnxCNPypcm1JxQQjhvUw
Ixs0rdmrIKE14qjuYzg0RIXAU4/D3RfTFJBWW7uiZx2ikzvQJII2+kowJcNATM5I
ET519DBf8IPlUWf/UaGQxLglxou3HEJFoSyrRDOXvsAodmu8AazIQd6PiDMXrCWP
0QIDAQAB
-----END PUBLIC KEY-----
'''
# 외부 공개용
print()
print("private Key : ")
print(privKey)

print("\n")
print("public key : PEM Version")
print(publicKey)

print("\n")
print("public key")
# print(publicKey.exportKey("PEM"))e


print("\n")
print("keydata : ")
# print(publicKey.keydata) 
# print(f"n : {publicKey.n}") # n값
# print(f"e : {publicKey.e}") # e값


# 암호화할 원문
plainText = 'This is Plain text. It will be encrypted using RSA.'
print("\n")
print("원문 :")
print(plainText)

# # 공개키로 원문을 암호화한다.
# cipherText = publicKey.encrypt(plainText.encode(), 10)
# print("\n")
# print("암호문 :")
# print()
# print(cipherText[0].hex())

# Private key를 소유한 수신자는 자신의 Private key로 암호문을 해독한다.
# pubKey와 쌍을 이루는 privKey 만이 이 암호문을 해독할 수 있다.
# key = RSA.importKey(privKey)
# plainText2 = key.decrypt("A+aIKmgmRtJmJhGRJM35v00/+x92yOOG7ldt63aq7oxFjNaFj6ojyAq4amdobK2RUiJ9hS5BPaHHS6LnlEnXMJQaBHZ2/rIOdUVVr571QOGlQSzjy4t2Mse8eLJ40W6ySa1QsS+dCFg231GzBtqv6B8CblTS1lKvdor6N1q2P2biE0QX2itYJ9K9NMVNyqOVeynPXJKa5mTHqHVFgJ6BrYXfDtpN9PdlcZIIgs/7AYc2YRXLBuBdZgBOQ0FpT7mjXEHiK3aC/VE2h3ygrnezp2huBRNjzNKNxr9NPs6sogZvMc2dEJ1KIsJtgFuA7CoHMGPzq1mzWQctrc8IvM9ezg==") 
# plainText2 = plainText2.decode()
# print("\n")
# print("해독문 :")
# print(plainText2)




plainText2 = "A+aIKmgmRtJmJhGRJM35v00/+x92yOOG7ldt63aq7oxFjNaFj6ojyAq4amdobK2RUiJ9hS5BPaHHS6LnlEnXMJQaBHZ2/rIOdUVVr571QOGlQSzjy4t2Mse8eLJ40W6ySa1QsS+dCFg231GzBtqv6B8CblTS1lKvdor6N1q2P2biE0QX2itYJ9K9NMVNyqOVeynPXJKa5mTHqHVFgJ6BrYXfDtpN9PdlcZIIgs/7AYc2YRXLBuBdZgBOQ0FpT7mjXEHiK3aC/VE2h3ygrnezp2huBRNjzNKNxr9NPs6sogZvMc2dEJ1KIsJtgFuA7CoHMGPzq1mzWQctrc8IvM9ezg=="

decryptor = PKCS1_OAEP.new(privKey)
decrypted = decryptor.decrypt(plainText2)
print("해독문 :")
print(decrypted)
