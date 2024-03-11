import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import base64
import json

# fN : firstName
# lf : lastName

payload = {
	"_fN_" : "VO MINH",
	"_lN_"  : "THUAN 2",
}

def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	
	reader = SimpleMFRC522()
	try:
		reader.write(json.dumps(payload))
	finally:
		GPIO.cleanup()
if __name__ == '__main__':
	print("__start__")
	main()