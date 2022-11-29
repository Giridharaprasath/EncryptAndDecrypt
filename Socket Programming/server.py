import socket

sock = socket.socket()
print("Socket Successfully Created")

port = 12345
sock.bind(('', port))
print("Socket bindind to %s" %{port})

sock.listen(5)
print("Socket is Listening")

while True:
  conn, addr = sock.accept()    
  print ('Got connection from', addr )
 
  conn.send('Thank you for connecting'.encode())
  conn.close()
   
  break