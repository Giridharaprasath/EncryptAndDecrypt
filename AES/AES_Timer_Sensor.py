from Crypto.Cipher import AES
import string, random, socket

sock = socket.socket()

port = 12345
sock.connect(('127.0.0.1', port))

key = sock.recv(1024)
print("Got Key From Server")

cipher_aes = AES.new(key, AES.MODE_EAX)

print("Sending nonce value to Server")
sock.sendall(cipher_aes.nonce)   # type: ignore

randomtext = ''.join(random.choices(string.ascii_letters, k = 64))
data = randomtext.encode()

encoded_data = cipher_aes.encrypt(data)

print("Sending Encrypted Data to Server")
sock.sendall(encoded_data)

sock.close()