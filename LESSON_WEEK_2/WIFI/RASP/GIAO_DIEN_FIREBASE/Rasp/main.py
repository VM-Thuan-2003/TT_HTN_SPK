import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import RPi.GPIO as GPIO

import time

led_1 = 2
led_2 = 3

on = 1
off = 0

path_url = "https://tt-htn-3-con-bao-default-rtdb.firebaseio.com/"
key = "./tt-htn-3-con-bao-firebase-adminsdk-bkjw3-a06594cb50.json"


time_curr = 0;
time_prev = 0;
time_delay = 0.5;

def control_led(name, state):
	GPIO.output(name, state)

def control(name,dt):
	if dt == "true":
		control_led(name, on)
		return "done"
	elif dt == "false":
		control_led(name, off)
		return "done"
	elif dt == '"inv"':
		if(GPIO.input(led_1) == on):
		        control_led(led_1,off)
		else:
		       control_led(led_1,on)

		if(GPIO.input(led_2) == on):
		        control_led(led_2,off)
		else:
		       control_led(led_2,on) 
		return "done"
	else:
		return "none"
def main():
	global time_curr, time_prev, time_delay

	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(led_1, GPIO.OUT)
	GPIO.setup(led_2, GPIO.OUT)

	GPIO.output(led_1, off)
	GPIO.output(led_2, off)

	cred = credentials.Certificate(key)
	firebase_admin.initialize_app(cred,{"databaseURL":path_url})

	while True:		

		time_curr = time.time()
		if(time_curr - time_prev > time_delay):
			time_prev = time_curr
			# print(time_delay)

			# fetch data from firebase
			data_led_1 = str(db.reference("control/led_1").get())
			data_led_2 = str(db.reference("control/led_2").get())
			data_led_inv = str(db.reference("control/led").get())

			print("led_1: ", data_led_1, "led_2: ", data_led_2, "led_inv: ", data_led_inv)

			res_led_1 = control(led_1,data_led_1)
			res_led_2 = control(led_2,data_led_2)	
			res_led_inv = control(any,data_led_inv)

			rst1 = db.reference("control/led_1").set(res_led_1)
			rst2 = db.reference("control/led_2").set(res_led_2)
			rst3 = db.reference("control/led").set(res_led_inv)

			# print(res_led_1, res_led_2, res_led_inv)

if __name__ == '__main__':
	print("__start__")
	main()