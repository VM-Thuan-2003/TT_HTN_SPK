import RPi.GPIO as GPIO

btn = 4
led = 5

state = 0

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(btn, GPIO.IN)
	GPIO.setup(led,GPIO.OUT)

def main():
	setup()
	while True:
	# this is code in loop
		state = GPIO.input(btn)
		#print("state: ",state)

		GPIO.output(led, state if GPIO.LOW else GPIO.HIGH)

		print("state: ", state, "led: ", GPIO.input(led))

if __name__ == __name__:
	print("__start__")
	main()
