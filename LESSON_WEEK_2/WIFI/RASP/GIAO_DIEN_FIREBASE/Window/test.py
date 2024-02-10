import tkinter as tk
from tkinter import ttk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Firebase:
    def __init__(self,cred, db):
        cred = credentials.Certificate(cred)
        firebase_admin.initialize_app(cred,{"databaseURL":db})
    def send_command(self,payload,addr,addr_child):
        ref = db.reference(addr)
        child_ref = ref.child(addr_child)
        child_ref.set(payload)
    def fetch_data(self,addr):
        ref = db.reference(addr)
        return ref.get()
class App:
    def __init__(self,root):

        self.root = root
        self.root.geometry("500x400")
        self.root.title("Ứng dụng kết nối Firebase")

        self.firebase = Firebase("./tt-htn-3-con-bao-firebase-adminsdk-bkjw3-a06594cb50.json","https://tt-htn-3-con-bao-default-rtdb.firebaseio.com/")

        self.label_log_int = ttk.Label(root, text="Log: ")
        self.label_log_int.place(x=250, y=200)

        self.label_log = ttk.Label(root, text=" ....")
        self.label_log.place(x=280, y=200)

        self.info()
        self.layout_main()
    def led_1_on(self):
        self.firebase.send_command(True,"control","led_1")
        self.label_log.config(text="led_1: "+ str(self.firebase.fetch_data("control/led_1")))
    def led_1_off(self):
        self.firebase.send_command(False,"control","led_1")
        self.label_log.config(text="led_1: "+ str(self.firebase.fetch_data("control/led_1")))
    def led_2_on(self):
        self.firebase.send_command(True,"control","led_2")
        self.label_log.config(text="led_2: "+ str(self.firebase.fetch_data("control/led_2")))
    def led_2_off(self):
        self.firebase.send_command(False,"control","led_2")
        self.label_log.config(text="led_2: "+ str(self.firebase.fetch_data("control/led_2")))
    def led_inv(self):
        self.firebase.send_command("inv","control","led")
        self.label_log.config(text="led: "+ str(self.firebase.fetch_data("control/led")))
    def layout_main(self):
        B11 = ttk.Button(self.root, text="LED 1 ON ",
                         width=20, command=self.led_1_on)
        B11.place(x=50, y=100)
        B12 = ttk.Button(self.root, text="LED 1 OFF",
                         width=20, command=self.led_1_off)
        B12.place(x=250, y=100)

        B21 = ttk.Button(self.root, text="LED 2 ON ",
                         width=20, command=self.led_2_on)
        B21.place(x=50, y=150)
        B22 = ttk.Button(self.root, text="LED 2 OFF",
                         width=20, command=self.led_2_off)
        B22.place(x=250, y=150)

        B3 = ttk.Button(self.root, text="INV", width=20, command=self.led_inv)
        B3.place(x=50, y=200)
    
    def info(self):
        label_1 = ttk.Label(self.root, foreground="red",
                            text="Bài tập: Ứng dụng giao tiếp Firebase")
        label_1.place(x=50, y=250)
        label_1.config(font=("Courier", 11))
        label_2 = ttk.Label(self.root, text="Tên nhóm: 3 con báo")
        label_2.place(x=50, y=274)
        label_2.config(font=("Courier", 14))
        label_3 = ttk.Label(
            self.root, text="Thành viên 1: Võ Minh Thuận - MSSV: 21161366")
        label_3.place(x=50, y=300)
        label_4 = ttk.Label(
            self.root, text="Thành viên 2: Lê Quang Thương - MSSV: 21161363")
        label_4.place(x=50, y=320)
        label_5 = ttk.Label(
            self.root, text="Thành viên 3: Trần Thị Xuân Hy - MSSV: 21161323")
        label_5.place(x=50, y=340)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()