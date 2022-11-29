import socket

sock = socket.socket()

port = 12345
sock.connect(('127.0.0.1', port))

print(sock.recv(1024).decode())

sock.close()