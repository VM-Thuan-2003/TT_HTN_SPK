import RPi.GPIO as GPIO

led_green = 2
led_yellow = 3
led_red = 4

pin_sensor = 14

def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin_sensor, GPIO.IN)

	while True:
		state = GPIO.input(pin_sensor)
		print("state", state)

if __name__ == __name__:
	print("__start__")
	main()