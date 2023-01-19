from Crypto.Cipher import DES
import string, random, socket

sock = socket.socket()

port = 12345
sock.connect(('127.0.0.1', port))

key = sock.recv(1024)
print("Got Key From Server")

cipher_des = DES.new(key, DES.MODE_EAX)

print("Sending nonce value to Server")
sock.sendall(cipher_des.nonce)   # type: ignore

randomtext = ''.join(random.choices(string.ascii_letters, k = 10000000))
data = randomtext.encode()

encoded_data = cipher_des.encrypt(data)

print("Sending Encrypted Data to Server")
sock.sendall(encoded_data)

sock.close()