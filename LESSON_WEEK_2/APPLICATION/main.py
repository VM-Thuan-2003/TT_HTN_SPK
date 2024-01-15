import bluetooth

import RPi.GPIO as GPIO

led = 2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
host = ""
port = 1
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Bluetooth Socket Created')

try:
    server.bind((host, port))
    print("Bluetooth Binding Completed")
except:
    print("Bluetooth Binding Failed")
    
server.listen(5) # One connection at a time
client, address = server.accept()
print("Connected To", address)
print("Client:", client)

try:
    while True:
        data = client.recv(1024)
        print(data)
        if data == "1":
            GPIO.OUTPUT(led,1)
            send_data = "Light On"
        elif data == "0":
            GPIO.OUTPUT(led,0)
            send_data = "Light Off"
        else:
            send_data = "Type 1 or 0"

        client.send(send_data)
except:
    GPIO.cleanup()
    client.close()
    server.close()