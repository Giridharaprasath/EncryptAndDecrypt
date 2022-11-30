import socket

from Crypto.Cipher import AES
from Crypto import Random

key = Random.get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

data = "Welcome to copyassignment.com!".encode()

nonce = cipher.nonce  # type: ignore

ciphertext = cipher.encrypt(data)

print("Cipher text:", ciphertext)

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

plaintext = cipher.decrypt(ciphertext)
print("Plain text:", plaintext.decode())