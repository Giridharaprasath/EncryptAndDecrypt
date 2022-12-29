from random import randint
import socket

from Crypto.Cipher import Blowfish
import time

sock = socket.socket()

port = 12345
sock.connect(('127.0.0.1', port))

key = sock.recv(1024)
print("Got Key From Server")

while True:
    cipher_blowfish = Blowfish.new(key, Blowfish.MODE_EAX)

    print("Sending nonce value to Server")
    sock.sendall(cipher_blowfish.nonce)   # type: ignore

    data = str(randint(0, 1000))

    encoded_data = cipher_blowfish.encrypt(data.encode())

    print("Sending Encrypted Data to Server: ", data)
    sock.sendall(encoded_data)
    time.sleep(2)

sock.send("STOP".encode())
sock.close()