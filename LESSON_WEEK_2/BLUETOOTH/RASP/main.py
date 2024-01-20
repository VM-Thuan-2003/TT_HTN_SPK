import RPi.GPIO as GPIO

import bluetooth

def control_led(name, state):
        GPIO.output(name, state)

off = 0
on  = 1

led_1 = 2
led_2 = 3

port = 1
host = ""

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)

GPIO.output(led_1, off)
GPIO.output(led_2, off)

server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

try:
        server.bind((host, port))
        print("Bluetooth Binding Completed")
except:
        print("Bluetooth Binding Failed")

server.listen(1)

client, address = server.accept()
print("Connected To", address)
print("Client:", client)

try:
        while True:
                data = client.recv(1024).decode('utf-8')
                print(data)
                
                if data == "led_1_on":
                        control_led(led_1,on)
                        send_data = "led_1 is on"
                elif data == "led_1_off":
                        control_led(led_1,off)
                        send_data = "led_1 is off"
                elif data == "led_2_on":
                        control_led(led_2,on)
                        send_data = "led_2 is on"
                elif data == "led_2_off":
                        control_led(led_2,off)
                        send_data = "led_2 is off"
                elif data == "led_inv":
                        if(GPIO.input(led_1) == on):
                                control_led(led_1,off)
                        else:
                               control_led(led_1,on)

                        if(GPIO.input(led_2) == on):
                                control_led(led_2,off)
                        else:
                               control_led(led_2,on) 

                        send_data = "led is inv - " + str(GPIO.input(led_1)) + " - " + str(GPIO.input(led_2))
                else:
                        send_data = "nhap lai....."


                client.send(send_data.encode("utf-8"))
except:
        GPIO.cleanup()

        client.close()
        server.close()
