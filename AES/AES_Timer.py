from timeit import default_timer as timer
from Crypto.Cipher import AES
from Crypto import Random
import string, random


key = Random.get_random_bytes(16)

cipher = AES.new(key, AES.MODE_EAX)

randomtext = ''.join(random.choices(string.ascii_letters, k = 64))
plaintext = randomtext.encode()

nonce = cipher.nonce  # type: ignore

startTime = timer()

msg = cipher.encrypt(plaintext)

endTime = timer()

print((endTime - startTime) * 1000.0, ' ms to encrypt')

#print("PlainText: ", randomtext)
#print("EncodedText: ", msg)

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

startTime = timer()

text = cipher.decrypt(msg)

endTime = timer()

decryptTime = (endTime - startTime) * 1000.0
print(decryptTime, ' ms to decrypt')