from Crypto.Cipher import Blowfish
from Crypto import Random

from timeit import default_timer as timer
import random, string

key = Random.get_random_bytes(16)

randomtext = ''.join(random.choices(string.ascii_letters, k = 10000000))
plaintext = randomtext.encode()

cipher = Blowfish.new(key, Blowfish.MODE_EAX)
nonce = cipher.nonce # type: ignore

startTime = timer()

encoded_data = cipher.encrypt(plaintext)
#print("Cipher text:", encoded_data)

endTime = timer()

print((endTime - startTime) * 1000.0, ' ms to encrypt')

cipher = Blowfish.new(key, Blowfish.MODE_EAX, nonce = nonce)

startTime = timer()

decoded_data = cipher.decrypt(encoded_data)
#print("Plain text:", decoded_data)

endTime = timer()

decryptTime = (endTime - startTime) * 1000.0
print(decryptTime, ' ms to decrypt')