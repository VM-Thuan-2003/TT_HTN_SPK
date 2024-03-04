import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	
	reader = SimpleMFRC522()
	try:
		id, text = reader.read()
		print(id, text)
	finally:
		GPIO.cleanup()
if __name__ == '__main__':
	print("__start__")
	main()