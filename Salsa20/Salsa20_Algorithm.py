from Crypto.Cipher import Salsa20
from Crypto import Random

key = Random.get_random_bytes(32)

cipher = Salsa20.new(key)

plaintext = b'Hello this is encrypted using Salsa20'
nonce = cipher.nonce  # type: ignore
msg = cipher.encrypt(plaintext)

print(msg)

cipher = Salsa20.new(key, nonce=nonce)
text = cipher.decrypt(msg)

print(text)