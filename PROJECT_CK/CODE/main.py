from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import serial
import json
from time import sleep

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

pin_rst = 6

no = True
yes = False

state_read_checkin  = no
state_read_checkout = no

state_read_done_checkin  = no
state_read_done_checkout = no

data_firstName = ""
data_lastName  = ""



class SerialData():
	def __init__(self, url, speed):
		self.ser = serial.Serial(url, speed, timeout=1)
		self.data = ""
		self.state_start = no
	def __read__(self):
		dt = self.ser.readline().decode('utf-8').strip()
		if dt:
			self.data = dt
			return self.data
		else:
			return None
	def __write__(self, dt):
		# dt type is string
		payload = ""
		payload = str.encode(dt + "\n")
		self.ser.write(payload)
	def __handel_serial__(self):
		data = SerialData.__read__(self)
		print(data)
	def __handel_serial_start__(self):
		data = SerialData.__read__(self)
		if data:
			if(data == "__Arduino_start__"):
				self.state_start = yes
		return self.state_start
if __name__ == '__main__':
	try:
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pin_rst, GPIO.OUT)

		reader = SimpleMFRC522()
		ser = SerialData('/dev/ttyUSB0',9600)
		while True:
			if(ser.__handel_serial_start__() == yes):
				print("start")
			
	except KeyboardInterrupt:
	    GPIO.cleanup()