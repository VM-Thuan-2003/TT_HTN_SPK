import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import base64
import json

# gpg --gen-random --armor 1 18 -> to create security_code

security_code = "jPCufN8Qd+o="

# secr is security_code
# lvl is level
# st is state

payload = {
	"secr":security_code,
	"lvl" : "client",
	# "st": "NONE"
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