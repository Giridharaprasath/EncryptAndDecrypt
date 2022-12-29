from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

random_gen = Random.new().read
key = RSA.generate(1024, random_gen)
publickey = key.publickey()

cipher_rsa = PKCS1_OAEP.new(publickey)

plaintext = b'Hello this is encrypted using PKCS#1 OAEP RSA'
encoded_data = cipher_rsa.encrypt(plaintext)
print('Encoded Data: ', encoded_data)

cipher_rsa = PKCS1_OAEP.new(key)
decoded_data = cipher_rsa.decrypt(encoded_data)
print('Decoded Data: ', decoded_data.decode()) 