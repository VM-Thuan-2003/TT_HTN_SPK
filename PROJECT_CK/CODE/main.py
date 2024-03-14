from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import serial
import json
from time import sleep

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

pin_rst = 6

yes = True
no = False

ModeVao = False
ModeRa = True

state_mode = False  # False -> Vao | True -> Ra


class Firebase():
    def __init__(self):
        path_url = "https://final-project-tthtn-default-rtdb.firebaseio.com/"
        key = "./final-project-tthtn-firebase-adminsdk-uf94u-be3a4ed142.json"
        cred = credentials.Certificate(key)
        firebase_admin.initialize_app(cred, {"databaseURL": path_url})
        self.path_ssid = "lineSlot/"

    def __write__(self, addr, payload):
        db.reference(self.path_ssid + addr).set(payload)

    def __read__(self, addr):
        ref = db.reference(self.path_ssid+addr)
        snapshot = ref.get()
        if snapshot is not None:
            # print("__snapshot__", snapshot)
            return True, snapshot
        else:
            return False, None

    def __check_init__(self):
        pass


class LineSlot():
    def __init__(self, numLine, slotInLine, fireBase_):
        self.numLine = numLine
        self.slotInLine = slotInLine
        self.total = self.numLine * self.slotInLine
        lineA = [None, None, None, None, None]
        lineB = [None, None, None, None, None]
        lineC = [None, None, None, None, None]
        self.line = [lineA, lineB, lineC]
        self.empty_slot = 0
        self.list_slot_empty = []
        self.fireBase = fireBase_
        LineSlot.__check_init__(self)

    def __check_init__(self):
        isData, data_read = self.fireBase.__read__(
            "list_slot")  # check if have data save in firebase
        if isData is False:
            # write data empty slot and list slot init to firebase
            self.fireBase.__write__(
                "empty_slot", LineSlot.__check_empty_slot__(self))
            self.fireBase.__write__(
                "list_slot", LineSlot.__read_all_slot__(self))
        else:
            # write data init from firebase into rasp
            for i in range(len(data_read)):
                dt = data_read[i].split("-")
                x = int(dt[0])
                y = int(dt[1])
                pl = dt[2]
                self.line[x][y] = pl
            isDataE, data_read_E = self.fireBase.__read__(
                "empty_slot")  # check if have data save in firebase
            if isDataE is True:
                self.empty_slot = data_read_E[0]
                self.list_slot_empty = data_read_E[1]
                # print(data_read_E)

    def __check_empty_slot__(self):
        list_slot_empty_t = []
        empty_slot_t = 0
        for i in range(len(self.line)):
            for y in range(len(self.line[i])):
                if self.line[i][y] is None or self.line[i][y] == "None":
                    list_slot_empty_t.append(str(i) + "-" + str(y))
                    empty_slot_t = empty_slot_t + 1
        self.empty_slot = empty_slot_t
        self.list_slot_empty = list_slot_empty_t
        return self.empty_slot, self.list_slot_empty

    def __read_all_slot__(self):
        slot = []
        for i in range(len(self.line)):
            for y in range(len(self.line[i])):
                slot.append(str(i) + "-" + str(y) + "-" + str(self.line[i][y]))
        return slot

    def __check_data_slot(self, dt):
        for i in range(len(self.line)):
            for y in range(len(self.line[i])):
                if dt == self.line[i][y]:
                    return True, str(i) + "-" + str(y)
        return False, None

    def __add_slot__(self, payload):
        if len(self.list_slot_empty) > 0:
            if (LineSlot.__check_data_slot(self, payload)[0] is False):
                data = self.list_slot_empty[0].split("-")
                self.list_slot_empty.remove(self.list_slot_empty[0])
                x = int(data[0])
                y = int(data[1])
                self.line[x][y] = payload
                return True, data[0] + "-" + data[1]
            return False, "duplicate id"
        return False, "full slot"

    def __remove_slot__(self, payload):
        state, data = LineSlot.__check_data_slot(self, payload)
        if state is True:
            x = int(data.split("-")[0])
            y = int(data.split("-")[1])
            self.line[x][y] = "None"
            return True, "Removed Id"
        return False, "No Found Id"


class Rfid():
    def __init__(self):
        self.reader = SimpleMFRC522()
        self.flag_read_rfid = 0

    def __read__(self):
        if self.flag_read_rfid == 1:
            self.flag_read_rfid = 0
            try:
                id, text = self.reader.read()
                return id, text
            except Exception as e:
                Rfid.__set_flag_read_rfid__(self)
                # raise e
                # id, text = Rfid.__read__(self)
                # return id, text
        else:
            return None, None

    def __set_flag_read_rfid__(self):
        self.flag_read_rfid = 1

    def __reset_flag_read_rfid__(self):
        self.flag_read_rfid = 0


class SerialData():
    def __init__(self, url, speed):
        self.ser = serial.Serial(url, speed, timeout=1)
        self.data = ""
        self.state_start = no

    def __read__(self):
        dt = self.ser.readline().decode('utf-8').strip()
        if dt:
            self.data = dt
            return self.data
        else:
            return None

    def __write__(self, dt):
        # dt type is string
        payload = str.encode(dt + "\n")
        self.ser.write(payload)

    def __handel_serial_start__(self):
        if self.state_start == no:
            data = SerialData.__read__(self)
            if data:
                if (data == "__Arduino_start__"):
                    self.state_start = yes
                    print("__log__: start begin")
        return self.state_start


if __name__ == '__main__':
    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_rst, GPIO.OUT)

        reader = SimpleMFRC522()
        ser = SerialData('/dev/ttyUSB0', 9600)
        rfid = Rfid()
        fireBase = Firebase()
        lineSlot = LineSlot(3, 5, fireBase)
        print(lineSlot.__check_empty_slot__())
        while True:
            if (ser.__handel_serial_start__() == yes):
                data = ser.__read__()
                if data is not None:
                    print("__log__: ", data)
                    if data == "modeVao":
                        state_mode = ModeVao
                    elif data == "modeRa":
                        state_mode = ModeRa
                    elif data == "ready_input_gate" or data == "ready_output_gate":
                        rfid.__set_flag_read_rfid__()
                else:
                    # No data
                    id, text = rfid.__read__()
                    if (id is not None and text is not None):
                        print(id, text)
                        try:
                            lastName = json.loads(text)["_lN_"]
                            firstName = json.loads(text)["_fN_"]
                            fullName = firstName + lastName
                            if (state_mode == ModeVao):
                                isDoneAdd, data_add = lineSlot.__add_slot__(
                                    str(id)+","+fullName)
                                ser.__write__(data_add)
                                if isDoneAdd is True:
                                    fireBase.__write__(
                                        "list_slot", lineSlot.__read_all_slot__())
                                    fireBase.__write__(
                                        "empty_slot", lineSlot.__check_empty_slot__())
                            else:
                                isDoneRmv, data_rmv = lineSlot.__remove_slot__(
                                    str(id)+","+fullName)
                                ser.__write__(data_rmv)
                                if isDoneRmv is True:
                                    fireBase.__write__(
                                        "list_slot", lineSlot.__read_all_slot__())
                                    fireBase.__write__(
                                        "empty_slot", lineSlot.__check_empty_slot__())
                        except Exception as e:
                            raise e

    except KeyboardInterrupt:
        GPIO.cleanup()
