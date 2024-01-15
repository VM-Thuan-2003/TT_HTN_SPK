import RPi.GPIO as GPIO
from time import sleep

btn = 26

led_green = 2
led_red = 3
led_yellow = 4

state = 0

count = 0

state_green = 0
state_red = 0
state_yellow = 0

# Broadcom pin-numbering scheme

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	GPIO.setup(led_green,GPIO.OUT)
	GPIO.setup(led_red,GPIO.OUT)
	GPIO.setup(led_yellow,GPIO.OUT)

	GPIO.output(led_green, 0)
	GPIO.output(led_red, 0)
	GPIO.output(led_yellow, 0)
def main():
	state_green = 0
	state_red = 0
	state_yellow = 0
	state = 0
	count = 0
	setup()
	while True:
	# this is code in loop
		state = GPIO.input(btn)
		if state:
			sleep(1)
			if(GPIO.input(btn)):
				count = count + 1
				if (count > 2):
					count = 0
				if count == 0:
					state_green = 1
					state_red = 0
					state_yellow = 0
				if count == 1:
					state_green = 0
					state_red = 1
					state_yellow = 0
				if count == 2:
					state_green = 0
					state_red = 0
					state_yellow = 1

		GPIO.output(led_green,state_green)
		GPIO.output(led_red,state_red)
		GPIO.output(led_yellow,state_yellow)
		print("state: ",state)

if __name__ == __name__:
	print("__start__")
	main()
