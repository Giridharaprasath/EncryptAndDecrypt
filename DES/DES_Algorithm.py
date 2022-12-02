from Crypto.Cipher import DES
from Crypto import Random

key = Random.get_random_bytes(8)

cipher = DES.new(key, DES.MODE_EAX)

plaintext = b'Hello this is encrypted using DES'
nonce = cipher.nonce  # type: ignore
msg = cipher.encrypt(plaintext)

print(msg)

cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
text = cipher.decrypt(msg)

print(text)