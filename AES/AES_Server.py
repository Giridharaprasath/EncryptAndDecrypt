import socket

from Crypto.Cipher import AES
from Crypto import Random

stop = b''

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

    print("Sending Key")
    conn.sendall(key)

    while True:
        nonce = conn.recv(1024)
        encoded_data = conn.recv(1024)
        
        if encoded_data == stop:
            conn.close()
            break   

        cipher_aes = AES.new(key, AES.MODE_EAX, nonce)
        decoded_data = cipher_aes.decrypt(encoded_data)
        print(decoded_data.decode())