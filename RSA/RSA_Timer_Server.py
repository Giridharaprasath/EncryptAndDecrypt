from timeit import default_timer as timer
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

random_gen = Random.new().read
key = RSA.generate(1024, random_gen)
publickey = key.publickey().export_key()

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

    #print("Sending Public Key")
    conn.sendall(publickey)
    i = 10
    while i > 0:
        
        encoded_data = conn.recv(1024)

        cipher_rsa = PKCS1_OAEP.new(key)
        decoded_data = cipher_rsa.decrypt(encoded_data)
        i -= 1

    endTime = timer() # * End Time after decrypting data

    totalTime = (endTime - startTime) * 1000.0
    print(totalTime , ' ms total time')
    # print(decoded_data.decode())  

    conn.close()
    break