import tkinter as tk
from tkinter import ttk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import base64 

# command is openssl rand -base64 24
security_code = "xs0xsdJHHg66BzDourjs9rst6DwDquHo"
# xs0xsdJHHg66BzDourjs9rst6DwDquHo
class Payload:
    def __init__(self, security_code):
        self.security_code = security_code
        self.header={
            "alg":"HS256",
            "typ":"JWT"
        }
    def encode(self,payload):
        return base64.b64encode(json.dumps(payload).encode("ascii")).decode("ascii")  + base64.b64encode(self.security_code.encode("ascii")).decode("ascii")
        # return  base64.b64encode(json.dumps(self.header).encode("ascii")).decode("ascii")  + base64.b64encode(json.dumps(payload).encode("ascii")).decode("ascii")  + base64.b64encode(self.security_code.encode("ascii")).decode("ascii")
    def decode(self,code):
        base64_bytes = code.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        return sample_string_bytes.decode("ascii")
    def payload(self,payload):
        return Payload.encode(self, payload)
class Firebase:
    def __init__(self,cred, db):
        cred = credentials.Certificate(cred)
        firebase_admin.initialize_app(cred,{"databaseURL":db})
        self.payload = Payload(security_code)
    def create(self,payload,addr,addr_child):
        ref = db.reference(addr)
        child_ref = ref.child(addr_child)
        child_ref.set(payload)
        pass
    def update(self,db,addr):
        pass
    def read(self,addr):
        pass
    def test(self):
        print(self.payload.payload("hello"))
        print(self.payload.decode("ImhlbGxvIg==MQ=="))
class App:
    def __init__(self,root):

        self.root = root
        self.root.geometry("500x400")
        self.root.title("Ứng dụng kết nối Bluetooth")

        self.firebase = Firebase("./tt-htn-3-con-bao-firebase-adminsdk-bkjw3-a06594cb50.json","https://tt-htn-3-con-bao-default-rtdb.firebaseio.com/")

        self.info()
        self.firebase.test()
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