from Crypto.Cipher import ARC2
from Crypto import Random

key = Random.get_random_bytes(16)

cipher = ARC2.new(key, ARC2.MODE_EAX)
nonce = cipher.nonce # type: ignore

plaintext = b'Hello this is encrypted using ARC2'

encoded_data = cipher.encrypt(plaintext)
print('Encoded Data: ', encoded_data)

cipher = ARC2.new(key, ARC2.MODE_EAX, nonce = nonce)
decoded_data = cipher.decrypt(encoded_data)
print('Decoded_Data: ', decoded_data)