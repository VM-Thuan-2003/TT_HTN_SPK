import serial
import time
import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import json

# flag_read_rfid = 0

class RfidModify():
	"""docstring for RfidModify"""
	def __init__(self):
		self.reader = SimpleMFRC522()
		self.flag_read_rfid = 0
	def readRfid(self):
		if self.flag_read_rfid == 1:
			self.flag_read_rfid = 0
			try:
				id, text = self.reader.read()
			except:
				return "id_none", "error in during read rfid"
			finally:
				return id, text
		else:
			return "id_none", "waiting reset flag_read_rfid to read again"
	def reset_flag_read_rfid(self):
		self.flag_read_rfid = 1

class FirebaseModify():
	def __init__(self):
		path_url = "https://final-project-tthtn-default-rtdb.firebaseio.com/"
		key = "./final-project-tthtn-firebase-adminsdk-uf94u-be3a4ed142.json"
		cred = credentials.Certificate(key)
		firebase_admin.initialize_app(cred,{"databaseURL":path_url})
		self.path_ssid = "ssid/"
		self.ConvectJson = self.StrtoJson
	def check_ssid(self, id):
		# true - co ton tai dia chi
		# false - khong co ton tai dia chi
		ref = db.reference(self.path_ssid+str(id))
		snapshot = ref.get()
		if snapshot is not None:
			return True
		else:
			return False
	def StrtoJson(self,payload):
		try:
			json_str = json.loads(payload)
		except:
			# string = '{"data":"'+str(payload)+'"}'
			json_str = payload
		finally:
			return json_str
	def create_ssid(self, id, payload):
		db.reference(self.path_ssid+str(id)).set(self.ConvectJson(payload))

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4, GPIO.OUT)

def main():
	setup()
	rfid     = RfidModify()
	firebase = FirebaseModify()
	while True:
		id, text = rfid.readRfid()
		if(id != "id_none"):
			print(id, text)
			current_time = datetime.datetime.now()
			print("Thời gian hiện tại là:", current_time)
			if(firebase.check_ssid(id) == True):
				print("da ton tai du lieu tren Firebase")
				# nhiem vu can la update trang thai ra vao
			else:
				print("da luu du lieu len Firebase")
				firebase.create_ssid(id,text)
				# nhiem vu can la luu du lieu va trang thai ra vao lan dau
		# print(GPIO.input(4))
		if GPIO.input(4) == 1:
			rfid.reset_flag_read_rfid()
if (__name__ == __name__):
	print("__start__")
	try:
		main()
	# When 'Ctrl+C' is pressed, the program destroy() will be  executed.
	except KeyboardInterrupt:
		GPIO.cleanup()