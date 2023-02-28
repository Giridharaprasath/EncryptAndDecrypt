from random import randint
import socket
from Crypto.Cipher import Salsa20
import time

import RPi.GPIO as GPIO

TRIG=14
ECHO=18
GPIO.setmode(GPIO.BCM)

sock = socket.socket()

port = 12345
sock.connect(('192.168.0.222', port))

key = sock.recv(1024)
#print("Got Key From Server")

#print("distance measurement in progress")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)
#print("waiting for sensor to settle")
time.sleep(0.2)
GPIO.output(TRIG,True)
time.sleep(0.00001)
GPIO.output(TRIG,False)
while GPIO.input(ECHO)==0:
    pulse_start=time.time()
while GPIO.input(ECHO)==1:
    pulse_end=time.time()
pulse_duration=pulse_end-pulse_start
distance=pulse_duration*17150
distance=round(distance,2)
#print("distance:",distance,"cm")

data= str(distance)

cipher_salsa20 = Salsa20.new(key)

#print("Sending nonce value to Server")
sock.sendall(cipher_salsa20.nonce)   # type: ignore

encoded_data = cipher_salsa20.encrypt(data.encode())

#print("Sending Encrypted Data to Server: ")
sock.sendall(encoded_data)
time.sleep(2)

sock.close()