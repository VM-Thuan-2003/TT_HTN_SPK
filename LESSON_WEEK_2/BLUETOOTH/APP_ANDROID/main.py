from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import socket

class BluetoothApp(App):
    def build(self):
        self.controller = BluetoothController("DC:A6:32:11:2A:6E", 1)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.connect_button = Button(text="Connect", on_press=self.connect)
        layout.add_widget(self.connect_button)

        self.disconnect_button = Button(text="Disconnect", on_press=self.disconnect, disabled=True)
        layout.add_widget(self.disconnect_button)

        self.command_entry = TextInput(hint_text="Enter command", multiline=False)
        layout.add_widget(self.command_entry)

        self.send_button = Button(text="Send Command", on_press=self.send_command, disabled=True)
        layout.add_widget(self.send_button)

        self.label_log_int = Label(text="Log:")
        layout.add_widget(self.label_log_int)

        self.label_log = Label(text="....")
        layout.add_widget(self.label_log)

        self.layout_main()
        self.info()

        return layout  # Make sure to return the layout here

    def connect(self, instance):
        try:
            self.controller.connect()
            self.connect_button.disabled = True
            self.disconnect_button.disabled = False
            self.send_button.disabled = False
            self.label_log.text = "Connected"

        except socket.error as e:
            self.label_log.text = f"Socket connection error: {e}"

    def disconnect(self, instance):
        self.controller.disconnect()
        self.connect_button.disabled = False
        self.disconnect_button.disabled = True
        self.send_button.disabled = True
        self.label_log.text = "Disconnected"

    def send_command(self, instance):
        command = self.command_entry.text
        log = self.controller.send_command(command)
        self.label_log.text = log

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
        label_1 = Label(text="Bài tập: Ứng dụng điều khiển led có đảo chiều", color=(1, 0, 0, 1), font_size=11)
        self.root.add_widget(label_1)

        label_2 = Label(text="Tên nhóm: 3 con báo", font_size=14)
        self.root.add_widget(label_2)

        label_3 = Label(text="Thành viên 1: Võ Minh Thuận - MSSV: 21161366")
        self.root.add_widget(label_3)

        label_4 = Label(text="Thành viên 2: Lê Quang Thương - MSSV: 21161363")
        self.root.add_widget(label_4)

        label_5 = Label(text="Thành viên 3: Trần Thị Xuân Hy - MSSV: 21161323")
        self.root.add_widget(label_5)

    def layout_main(self):
        B11 = Button(text="LED 1 ON", size_hint=(None, None), size=(200, 50), on_press=self.led_1_on)
        self.root.add_widget(B11)

        B12 = Button(text="LED 1 OFF", size_hint=(None, None), size=(200, 50), on_press=self.led_1_off)
        self.root.add_widget(B12)

        B21 = Button(text="LED 2 ON", size_hint=(None, None), size=(200, 50), on_press=self.led_2_on)
        self.root.add_widget(B21)

        B22 = Button(text="LED 2 OFF", size_hint=(None, None), size=(200, 50), on_press=self.led_2_off)
        self.root.add_widget(B22)

        B3 = Button(text="INV", size_hint=(None, None), size=(200, 50), on_press=self.led_inv)
        self.root.add_widget(B3)

class BluetoothController:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

if __name__ == "__main__":
    BluetoothApp().run()
