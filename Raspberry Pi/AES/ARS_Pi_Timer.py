from random import randint
from Crypto.Cipher import AES
from Crypto import Random
import time
from timeit import default_timer as timer

import RPi.GPIO as GPIO

TRIG=14
ECHO=18
GPIO.setmode(GPIO.BCM)

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

key = Random.get_random_bytes(16)

cipher_aes = AES.new(key, AES.MODE_EAX)

nonce = cipher.nonce  # type: ignore

startTime = timer()

encoded_data = cipher_aes.encrypt(data.encode())

endTime = timer()

print((endTime - startTime) * 1000.0, ' ms to encrypt')

#print("PlainText: ", randomtext)
#print("EncodedText: ", msg)

cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

startTime = timer()

text = cipher.decrypt(encoded_data)

endTime = timer()

decryptTime = (endTime - startTime) * 1000.0
print(decryptTime, ' ms to decrypt')