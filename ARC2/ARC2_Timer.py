from Crypto.Cipher import ARC2
from Crypto import Random
import string, random
from timeit import default_timer as timer

key = Random.get_random_bytes(16)

cipher = ARC2.new(key, ARC2.MODE_EAX)
nonce = cipher.nonce # type: ignore

randomtext = ''.join(random.choices(string.ascii_letters, k = 64))
plaintext = randomtext.encode()

startTime = timer()

encoded_data = cipher.encrypt(plaintext)
#print('Encoded Data: ', encoded_data)

endTime = timer()

print((endTime - startTime) * 1000.0, ' ms to encrypt')

cipher = ARC2.new(key, ARC2.MODE_EAX, nonce = nonce)

startTime = timer()

decoded_data = cipher.decrypt(encoded_data)
#print('Decoded_Data: ', decoded_data)

endTime = timer()
decryptTime = (endTime - startTime) * 1000.0
print(decryptTime, ' ms to decrypt')