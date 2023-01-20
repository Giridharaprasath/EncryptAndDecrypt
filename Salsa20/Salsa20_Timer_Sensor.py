from random import randint
import socket

from Crypto.Cipher import Salsa20
import time, string, random

sock = socket.socket()

port = 12345
sock.connect(('127.0.0.1', port))

key = sock.recv(1024)
print("Got Key From Server")

cipher_salsa20 = Salsa20.new(key)

print("Sending nonce value to Server")
sock.sendall(cipher_salsa20.nonce)   # type: ignore

randomtext = ''.join(random.choices(string.ascii_letters, k = 64))
data = randomtext.encode()

encoded_data = cipher_salsa20.encrypt(data)

print("Sending Encrypted Data to Server: ")
sock.sendall(encoded_data)
time.sleep(2)

sock.close()