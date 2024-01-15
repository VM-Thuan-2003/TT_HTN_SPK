import RPi.GPIO as GPIO
from time import sleep

btn = 26

led_green  = 2
led_red    = 3
led_yellow = 4

state = 0

def setup():

	state = 0

	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	GPIO.setup(led_green,GPIO.OUT)
	GPIO.setup(led_red,GPIO.OUT)
	GPIO.setup(led_yellow,GPIO.OUT)l

	GPIO.output(led_green, 0)
	GPIO.output(led_red, 0)
	GPIO.output(led_yellow, 0)

def main():
	setup()
	while True:
		state = GPIO.input(btn)
		GPIO.output(led_green,state)
		GPIO.output(led_red,state)
		GPIO.output(led_yellow,state)
		print("state: ",state)

if __name__ == __name__:
	print("__start__")
	main()
