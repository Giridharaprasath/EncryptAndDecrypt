from random import randint
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import time
from timeit import default_timer as timer

import RPi.GPIO as GPIO

TRIG=14
ECHO=18
GPIO.setmode(GPIO.BCM)

random_gen = Random.new().read
key = RSA.generate(2048, random_gen)
publickey = key.publickey()
cipher_rsa = PKCS1_OAEP.new(publickey)

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

startTime = timer()

encoded_data = cipher_rsa.encrypt(data.encode())

endTime = timer()

print((endTime - startTime) * 1000.0, ' ms to encrypt')

cipher_rsa = PKCS1_OAEP.new(key)

startTime = timer()

decoded_data = cipher_rsa.decrypt(encoded_data)

endTime = timer()

print((endTime - startTime) * 1000.0, ' ms to encrypt')