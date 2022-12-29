from Crypto.Cipher import Blowfish
from Crypto import Random

key = Random.get_random_bytes(16)

plaintext = b'Hello this is encrypted using Blowfish'

cipher = Blowfish.new(key, Blowfish.MODE_EAX)
nonce = cipher.nonce # type: ignore

encoded_data = cipher.encrypt(plaintext)
print("Cipher text:", encoded_data)

cipher = Blowfish.new(key, Blowfish.MODE_EAX, nonce = nonce)

decoded_data = cipher.decrypt(encoded_data)
print("Plain text:", decoded_data)