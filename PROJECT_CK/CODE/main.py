from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import serial
import json
from time import sleep

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

pin_rst = 6

yes = True
no  = False

ModeVao = False
ModeRa  = True

state_mode = False # False -> Vao | True -> Ra

class Firebase():
	def __init__(self):
		path_url = "https://final-project-tthtn-default-rtdb.firebaseio.com/"
		key = "./final-project-tthtn-firebase-adminsdk-uf94u-be3a4ed142.json"
		cred = credentials.Certificate(key)
		firebase_admin.initialize_app(cred,{"databaseURL":path_url})
		self.path_ssid = "lineSlot/"
	def __write__(self, addr, payload):
		db.reference(self.path_ssid + addr).set(payload)
	def __read__(self, addr):
		ref = db.reference(self.path_ssid+addr)
		snapshot = ref.get()
		if snapshot is not None:
			#print("__snapshot__", snapshot)
			return True, snapshot
		else:
			return False , None
	def __check_init__(self):
		pass
class LineSlot():
	def __init__(self, numLine, slotInLine, fireBase_):
		self.numLine  = numLine
		self.slotInLine = slotInLine
		self.total = self.numLine * self.slotInLine
		lineA = [None,None,None,None,None]
		lineB = [None,None,None,None,None]
		lineC = [None,None,None,None,None]
		self.line = [lineA, lineB, lineC]
		self.empty_slot = 0
		self.list_slot_empty = []
		self.fireBase = fireBase_
		LineSlot.__check_init__(self)
	def __check_init__(self):
		isData, data_read = self.fireBase.__read__("empty_slot")
		if isData is False:
			# write data init to firebase
			self.fireBase.__write__("empty_slot", LineSlot.__check_empty_slot__(self))
		else:
			# write data init from firebase into rasp
			self.empty_slot = data_read[0]
			self.list_slot_empty = data_read[1]

			print("__check_data__: ", "empty_slot", self.empty_slot, "list_slot_empty",self.list_slot_empty)

	def __check_empty_slot__(self):
		for i in range(len(self.line)):
			for y in range(len(self.line[i])):
				if self.line[i][y] is None:
					self.list_slot_empty.append(str(i) + "-" + str(y))
					self.empty_slot = self.empty_slot + 1;
		return self.empty_slot, self.list_slot_empty

	def __add_slot__(self,payload):
		if len(self.list_slot_empty) > 0:
			print(self.list_slot_empty[0])
			data = self.list_slot_empty[0].split("-")
			self.list_slot_empty.remove(self.list_slot_empty[0])
			x = int(data[0])
			y = int(data[1])
			self.line[x][y] = payload
			print(self.line)
			return True
		return False
class Rfid():
	def __init__(self):
		self.reader = SimpleMFRC522()
		self.flag_read_rfid = 0
	def __read__(self):
		if self.flag_read_rfid == 1:
			self.flag_read_rfid = 0
			try:
				id, text = self.reader.read()
				return id, text
			except Exception as e:
				rfid.__set_flag_read_rfid__()
				raise e
				return None, None
		else:
			return None, None
	def __set_flag_read_rfid__(self):
		self.flag_read_rfid = 1
	def __reset_flag_read_rfid__(self):
		self.flag_read_rfid = 0

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
		payload = str.encode(dt + "\n")
		self.ser.write(payload)
	def __handel_serial_start__(self):
		if self.state_start == no:
			data = SerialData.__read__(self)
			if data:
				if(data == "__Arduino_start__"):
					self.state_start = yes
					print("__log__: start begin")
		return self.state_start

if __name__ == '__main__':
	try:
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pin_rst, GPIO.OUT)

		reader = SimpleMFRC522()
		ser = SerialData('/dev/ttyUSB0',9600)
		rfid = Rfid()
		fireBase = Firebase()
		lineSlot = LineSlot(3,5,fireBase)
		print(lineSlot.__check_empty_slot__())
		while True:
			if(ser.__handel_serial_start__() == yes):
				data = ser.__read__()
				if data is not None:
					print("__log__: ", data)
					if   data == "modeVao":
						state_mode = ModeVao
					elif data == "modeRa" :
						state_mode = ModeRa
					elif data == "ready_input_gate" or data == "ready_output_gate":
						 rfid.__set_flag_read_rfid__()
				else:
					# No data
					id, text = rfid.__read__()
					if(id is not None and text is not None):
						print(id, text)
						try:
							lastName = json.loads(text)["_lN_"]
							firstName = json.loads(text)["_fN_"]
							if(state_mode == ModeVao):
								ser.__write__(str(id))
								lineSlot.__add_slot__(lastName)
							else:
								ser.__write__(str(id))
								lineSlot.__add_slot__(lastName)
						except Exception as e:
							raise e

			
	except KeyboardInterrupt:
	    GPIO.cleanup()