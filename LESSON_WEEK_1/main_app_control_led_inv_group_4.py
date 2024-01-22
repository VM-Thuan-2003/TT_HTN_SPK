from tkinter import *

import RPi.GPIO as GPIO
from time import sleep

led_1  = 2
led_2  = 3

height = 400
width = 500

window = Tk()
window.geometry("500x400")
window.title("ung dung dieu khien led")


def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(led_1,GPIO.OUT)
	GPIO.setup(led_2,GPIO.OUT)
	GPIO.output(led_1, 0)
	GPIO.output(led_2, 0)
	print("__start__")
	sleep(1)

def control_light(pin, state):
	GPIO.output(pin, state)

def control_light_1_off():
	control_light(led_1, 0)
	text_led_1 = Label(window, text = "State Led 1: " + str(GPIO.input(led_1)))
	text_led_1.place(x=50,y=10)

def control_light_1_on():
	control_light(led_1, 1)
	text_led_1 = Label(window, text = "State Led 1: " + str(GPIO.input(led_1)))
	text_led_1.place(x=50,y=10)

def control_light_2_off():
	control_light(led_2, 0)
	text_led_2 = Label(window, text = "State Led 2: " + str(GPIO.input(led_2)))
	text_led_2.place(x=250,y=10)

def control_light_2_on():
	control_light(led_2, 1)
	text_led_2 = Label(window, text = "State Led 2: " + str(GPIO.input(led_2)))
	text_led_2.place(x=250,y=10)

def control_light_inv():
	if(GPIO.input(led_1) == 1):
		control_light_1_off()
	else:
		control_light_1_on()

	if(GPIO.input(led_2) == 1):
		control_light_2_off()
	else:
		control_light_2_on()

def style_info():
	# height = 200 - width = 500
	label_1 = Label(window, fg="red",text = "Bài tập: Ứng dụng điều khiển led có đảo chiều")
	label_1.place(x=50,y=200)
	label_1.config(font =("Courier", 11))
	label_2 = Label(window, text = "Tên nhóm: 3 con báo")
	label_2.place(x=50,y=250)
	label_2.config(font =("Courier", 14))
	label_3 = Label(window, text = "Thành viên 1: Võ Minh Thuận - MSSV: 21161366")
	label_3.place(x=50,y=300)
	label_4 = Label(window, text = "Thành viên 2: Lê Quang Thương - MSSV: 21161363")
	label_4.place(x=50,y=320)
	label_5 = Label(window, text = "Thành viên 3: Trần Thị Xuân Hy - MSSV: 21161323")
	label_5.place(x=50,y=340)

def style_window():
	# height = 200 - width = 500
	
	text_led_1 = Label(window, text = "State Led 1: " + str(GPIO.input(led_1)))
	text_led_1.place(x=50,y=10)
	B1 = Button(window, text="LED 1 ON ", width=20, bg="green", fg="black", command=control_light_1_on)
	B1.place(x=50,y=50)
	B2 = Button(window, text="LED 1 OFF", width=20, bg="red", fg="black", command=control_light_1_off)
	B2.place(x=250,y=50)
	
	text_led_2 = Label(window, text = "State Led 2: " + str(GPIO.input(led_1)))
	text_led_2.place(x=250,y=10)
	B1 = Button(window, text="LED 2 ON ", width=20, bg="green", fg="black", command=control_light_2_on)
	B1.place(x=50,y=100)
	B2 = Button(window, text="LED 2 OFF", width=20, bg="red", fg="black", command=control_light_2_off)
	B2.place(x=250,y=100)

	B3 = Button(window, text="INV", width=20, bg="yellow", fg="black", command=control_light_inv)
	B3.place(x=50,y=150)

def main():
	setup()
	style_info()
	style_window()
	window.mainloop()

if __name__ == '__main__':
	main()