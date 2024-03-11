import serial
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

path_url = "https://tt-htn-3-con-bao-default-rtdb.firebaseio.com/"
key = "./tt-htn-3-con-bao-firebase-adminsdk-bkjw3-a06594cb50.json"

cred = credentials.Certificate(key)
firebase_admin.initialize_app(cred,{"databaseURL":path_url})

# Change the port parameter to match your Arduino's port
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# Give some time for the serial connection to be established
time.sleep(2)

try:
    print("__start__")
    while True:
        # Read data from Arduino
        data = ser.readline().decode('utf-8').strip()
        
        if data:    
            rst1 = db.reference("sensor/sr04").set(data)
            print("Arduino says:", data)

except KeyboardInterrupt:
    print("Closing the serial connection.")
    ser.close()
