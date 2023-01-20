import socket

from Crypto.Cipher import Blowfish
from Crypto import Random

from timeit import default_timer as timer

key = Random.get_random_bytes(16)

sock = socket.socket()
print("Socket Successfully Created")

port = 12345
sock.bind(('', port))
print("Socket bindind to %s" %{port})

sock.listen(5)
print("Socket is Listening")

while True:
    conn, addr = sock.accept()
    print("Got Connection from ", addr)

    startTime = timer()

    print("Sending Key")
    conn.sendall(key)

    nonce = conn.recv(1024)
    encoded_data = conn.recv(1024)

    cipher_blowfish = Blowfish.new(key, Blowfish.MODE_EAX, nonce)
    decoded_data = cipher_blowfish.decrypt(encoded_data)
    #print(decoded_data.decode())

    endTime = timer()
    totalTime = (endTime - startTime) * 1000.0
    print(totalTime, ' ms total time')

    conn.close()
    break