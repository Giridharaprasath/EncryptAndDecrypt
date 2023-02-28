import socket

from Crypto.Cipher import Salsa20
from Crypto import Random

from timeit import default_timer as timer

key = Random.get_random_bytes(32)

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
    i = 10
    while i > 0:
            
        nonce = conn.recv(1024)
        encoded_data = conn.recv(1024) 

        cipher_salsa20 = Salsa20.new(key, nonce)
        decoded_data = cipher_salsa20.decrypt(encoded_data)
        i -= 1
    #print(decoded_data.decode())

    endTime = timer()

    decryptTime = (endTime - startTime) * 1000.0
    print(decryptTime, ' ms total time')

    conn.close()
    break