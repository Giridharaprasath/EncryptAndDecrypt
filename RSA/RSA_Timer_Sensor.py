from random import randint
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time, string, random

sock = socket.socket()

port = 12345
sock.connect(('127.0.0.1', port))

publickey = RSA.import_key(sock.recv(1024))
#print("Got Public Key From Server")
cipher_rsa = PKCS1_OAEP.new(publickey)

data = b'5'
encoded_data = cipher_rsa.encrypt(data)
#print("Sending Encrypted Data to Server: ")
sock.sendall(encoded_data)

time.sleep(2)

sock.close()