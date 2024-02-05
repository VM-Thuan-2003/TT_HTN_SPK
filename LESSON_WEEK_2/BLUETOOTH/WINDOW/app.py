import tkinter as tk
from tkinter import ttk
import socket

log_label = ""

class BluetoothController:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None

    def connect(self):
        self.client_socket = socket.socket(
            socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.client_socket.connect((self.host, self.port))

    def send_command(self, command):
        if self.client_socket:
            self.client_socket.send(command.encode("utf-8"))
            return self.log_command()

    def disconnect(self):
        if self.client_socket:
            self.client_socket.close()

    def log_command(self):
        if self.client_socket:
            data = self.client_socket.recv(1024).decode('utf-8')
            if data:
                print(f"msg: {data}")
                return data
            return None


class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x400")
        self.root.title("Ứng dụng kết nối Bluetooth")

        # Thay đổi địa chỉ MAC và cổng theo yêu cầu
        self.controller = BluetoothController("B8:27:EB:0E:F2:0D", 1)

        self.connect_button = ttk.Button(
            root, text="Connect", command=self.connect)
        self.connect_button.place(x=50, y=50)

        self.disconnect_button = ttk.Button(
            root, text="Disconnect", command=self.disconnect, state=tk.DISABLED)
        self.disconnect_button.place(x=150, y=50)

        self.command_entry = ttk.Entry(root, width=20)
        self.command_entry.place(x=250, y=50)

        self.send_button = ttk.Button(
            root, text="Send Command", command=self.send_command_entry, state=tk.DISABLED)
        self.send_button.place(x=400, y=50)

        self.label_log_int = ttk.Label(root, text="Log: ")
        self.label_log_int.place(x=250, y=200)

        self.label_log = ttk.Label(root, text=" ....")
        self.label_log.place(x=280, y=200)

        self.layout_main()
        self.info()

    def connect(self):
        self.controller.connect()
        self.connect_button.configure(state=tk.DISABLED)
        self.disconnect_button.configure(state=tk.NORMAL)
        self.send_button.configure(state=tk.NORMAL)
        self.label_log.config(text="Connected")

    def disconnect(self):
        self.controller.disconnect()
        self.connect_button.configure(state=tk.NORMAL)
        self.disconnect_button.configure(state=tk.DISABLED)
        self.send_button.configure(state=tk.DISABLED)
        self.label_log.config(text="Disconnected")

    def send_command(self, command):
        log = self.controller.send_command(command)
        self.label_log.config(text=log)

    def send_command_entry(self):
        command = self.command_entry.get()
        log = self.controller.send_command(command)
        self.label_log.config(text=log)

    def led_1_on(self):
        self.send_command("led_1_on")

    def led_1_off(self):
        self.send_command("led_1_off")

    def led_2_on(self):
        self.send_command("led_2_on")

    def led_2_off(self):
        self.send_command("led_2_off")

    def led_inv(self):
        self.send_command("led_inv")

    def info(self):
        label_1 = ttk.Label(self.root, foreground="red",
                            text="Bài tập: Ứng dụng điều khiển led có đảo chiều")
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


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
