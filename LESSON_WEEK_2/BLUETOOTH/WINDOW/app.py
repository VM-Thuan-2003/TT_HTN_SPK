from tkinter import *
import socket
from bluetooth import *

height = 500
width  = 600


window = Tk()
window.geometry("600x500")
window.title("ung dung ket noi Bluetooth")

def text(text, place, font, size, color="black"):
	txt = Label(window, text = text )
	txt.place(x=place[0],y=place[1])
	txt.config(font=(str(font),size), fg=color)

def info():
	text("Đề tài: App Điều Khiển Raspberry qua Bluetooth",(10,height - 160),"Arial",12,color="red")
	text("Nhóm: Nhóm 4",(10,height - 130),"Arial",12)
	text("Thành viên:",(10,height - 130 + 24*1),"Arial",12)
	text("* Võ Minh Thuận    - 21161366",(12,height - 130 + 24*2),"Arial",12)
	text("* Trần Thị Xuân Hy - 21161367",(12,height - 130 + 24*3),"Arial",12)
	text("* Lê Quang Thương  - 21161323",(12,height - 130 + 24*4),"Arial",12)

def scan_bluetooth():
	nearby_devices = discover_devices(lookup_names = True)
	len_nearby_devices = len(nearby_devices)
	if len_nearby_devices > 0: 
		for i in range(len_nearby_devices):
			addr = nearby_devices[i][0]
			name = nearby_devices[i][1]
			print(name, addr)
			text(name + " - " + addr, (10, 20*(i+1)), "Arial", 10)
def layout_main():
	scanBlue = Button(window, text="Scan Bluetooth", width=20, bg="gray", fg="black",command=scan_bluetooth)
	scanBlue.place(x=10, y=10)
def main():
	info()
	layout_main()
	window.mainloop()
if __name__ == '__main__':
	print("__start__")
	main()