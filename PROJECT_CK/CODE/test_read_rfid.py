import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import json
import serial

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	
	reader = SimpleMFRC522()

	# Change the port parameter to match your Arduino's port
	ser = serial.Serial('/dev/ttyUSB0', 9600)
	while True:
		try:
			id, text = reader.read()
			print(id, text)
			json_str = json.loads(str(text))
			ser.write(str.encode(json_str["_lN_"]))
		finally:
			GPIO.cleanup()
if __name__ == '__main__':
	print("__start__")
	main()