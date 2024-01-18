from tkinter import *
import socket

window = Tk()
window.geometry("500x400")
window.title("ung dung ket noi Bluetooth")

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("B8:27:EB:0E:F2:0D",1))

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
	label_5 = Label(window, text = "Thành viên 3: Trần Thị Xuân Hy - MSSV: 21161342")
	label_5.place(x=50,y=340)

def style_window():
	# height = 200 - width = 500
    pass

def send_payload(name, msg):
    payload = {
        "name": name,
        "msg": msg
    }
    client.send(str(payload).encode("utf-8"))

def main():
    style_info()
    style_window()
    window.mainloop()

if __name__ == '__main__':
	main()