import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import base64
import json

# gpg --gen-random --armor 1 18 -> to create security_code

security_code = "3w+P+H3N9ENQUD6urJwhCxU/"
payload = {
	"security_code":security_code,
	"level" : "client",
}

def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	
	reader = SimpleMFRC522()
	try:
		
		id = "0355524273-21161366 - "
		text = "vo minh thuan"
		reader.write(json.dumps(payload))
	finally:
		GPIO.cleanup()
if __name__ == '__main__':
	print("__start__")
	main()