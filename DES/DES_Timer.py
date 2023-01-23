from timeit import default_timer as timer
from Crypto.Cipher import DES
from Crypto import Random
import string, random


key = Random.get_random_bytes(8)

cipher = DES.new(key, DES.MODE_EAX)

randomtext = ''.join(random.choices(string.ascii_letters, k = 64))
plaintext = randomtext.encode()

nonce = cipher.nonce  # type: ignore

startTime = timer()

msg = cipher.encrypt(plaintext)

endTime = timer()

encryptTime = (endTime - startTime) * 1000.0
print(encryptTime, ' ms to encrypt')

cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)

startTime = timer()

text = cipher.decrypt(msg)

endTime = timer()

decryptTime = (endTime - startTime) * 1000.0
print(decryptTime, ' ms to decrypt')