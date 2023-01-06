from Crypto.Cipher import DES
import hashlib
import base64

key=input("Key is:")
#if l<32:
#  l=32-len(key);
#  key+=(l*"A")
key.encode('utf-8')
m=hashlib.md5(key)
key=m.digest()

  

crypter=DES.new(key[:8],DES.MODE_OFB)

plain_text=input("Plain text is")
print("It is ",plaint_text)
plain_text=plain_text.encode('utf-8)
ciphertext=crypter.encrypt(plain_text)
encodestr=base64.b64encode(ciphertext).hex()
print("Encoded string is",encode_string)
