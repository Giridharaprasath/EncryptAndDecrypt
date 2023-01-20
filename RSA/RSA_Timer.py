from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import string, random
from timeit import default_timer as timer

random_gen = Random.new().read
key = RSA.generate(1024, random_gen)
publickey = key.publickey()

cipher_rsa = PKCS1_OAEP.new(publickey)

randomtext = ''.join(random.choices(string.ascii_letters, k = 64))
plaintext = randomtext.encode()

startTime = timer()

encoded_data = cipher_rsa.encrypt(plaintext)

endTime = timer()

print((endTime - startTime) * 1000.0, ' ms to encrypt')

cipher_rsa = PKCS1_OAEP.new(key)

startTime = timer()

decoded_data = cipher_rsa.decrypt(encoded_data)

endTime = timer()

print((endTime - startTime) * 1000.0, ' ms to encrypt')