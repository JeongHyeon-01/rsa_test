from Crypto.PublicKey import RSA
from Crypto import Random 

# Private key와 Public key 쌍을 생성한다.
# Private key는 소유자가 보관하고, Public key는 공개한다. 


random_generator = Random.new().read

keyPair = RSA.generate(1024,random_generator)
privKey = keyPair.exportKey()   # 키 소유자 보관용
publicKey = keyPair.publickey()    # 외부 공개용
print()
print("private Key : ")
print(privKey)

print("\n")
print("public key : ")
print(publicKey)
print(publicKey.validate)
print(publicKey.implementation)


print("\n")
print("keydata : ")
print(publicKey.keydata) 
print(f"n : {publicKey.n}") # n값
print(f"e : {publicKey.e}") # e값


# 암호화할 원문
plainText = 'This is Plain text. It will be encrypted using RSA.'
print("\n")
print("원문 :")
print(plainText)

# 공개키로 원문을 암호화한다.
cipherText = publicKey.encrypt(plainText.encode(), 10)
print("\n")
print("암호문 :")
print()
print(cipherText[0].hex())

# Private key를 소유한 수신자는 자신의 Private key로 암호문을 해독한다.
# pubKey와 쌍을 이루는 privKey 만이 이 암호문을 해독할 수 있다.
key = RSA.importKey(privKey)
plainText2 = key.decrypt(cipherText) 
plainText2 = plainText2.decode()
print("\n")
print("해독문 :")
print(plainText2)