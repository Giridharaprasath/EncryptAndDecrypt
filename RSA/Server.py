import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

stop = b''

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

    print("Sending Public Key")
    conn.sendall(publickey)

    while True:
        encoded_data = conn.recv(1024)
        
        if encoded_data == stop:
            conn.close()
            break

        cipher_rsa = PKCS1_OAEP.new(key)
        decoded_data = cipher_rsa.decrypt(encoded_data)
        print(decoded_data.decode())    