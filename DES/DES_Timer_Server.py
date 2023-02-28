from timeit import default_timer as timer
import socket

from Crypto.Cipher import DES
from Crypto import Random

key = Random.get_random_bytes(8)

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

    startTime = timer() # * Start Time at client successful connection

    print("Sending Key")
    conn.sendall(key)
    i = 10
    while i > 0:
        nonce = conn.recv(1024)
        encoded_data = conn.recv(1024)

        cipher_des = DES.new(key, DES.MODE_EAX, nonce)

        decoded_data = cipher_des.decrypt(encoded_data)
        i -= 1
    
    endTime = timer() # * End Time after decrypting data

    totalTime = (endTime - startTime) * 1000.0
    print(totalTime , ' ms total time')
    #print(decoded_data.decode())
    
    conn.close()
    break