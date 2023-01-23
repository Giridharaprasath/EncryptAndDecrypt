from Crypto.Cipher import Salsa20
from Crypto import Random
from timeit import default_timer as timer
import string, random

key = Random.get_random_bytes(32)

cipher = Salsa20.new(key)

randomtext = ''.join(random.choices(string.ascii_letters, k = 64))
plaintext = randomtext.encode()
nonce = cipher.nonce  # type: ignore

startTime = timer()

msg = cipher.encrypt(plaintext)

endTime = timer()

print((endTime - startTime) * 1000.0, ' ms to encrypt')
#print(msg)

cipher = Salsa20.new(key, nonce=nonce)

startTime = timer()
text = cipher.decrypt(msg)

#print(text)
endTime = timer()

decryptTime = (endTime - startTime) * 1000.0
print(decryptTime, ' ms to decrypt')