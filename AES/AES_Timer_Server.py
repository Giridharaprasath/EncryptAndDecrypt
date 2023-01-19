from timeit import default_timer as timer
import socket

from Crypto.Cipher import AES
from Crypto import Random

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

    startTime = timer() # * Start Time at client successful connection

    print("Sending Key")
    conn.sendall(key)

    nonce = conn.recv(1024)
    encoded_data = conn.recv(1024)

    cipher_aes = AES.new(key, AES.MODE_EAX, nonce)

    decoded_data = cipher_aes.decrypt(encoded_data)
    
    endTime = timer() # * End Time after decrypting data

    totalTime = (endTime - startTime) * 1000.0
    print(totalTime , ' ms total time')
    #print(decoded_data.decode())
    
    conn.close()
    break