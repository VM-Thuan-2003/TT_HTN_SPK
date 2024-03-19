#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>

#define pinServo  A0
#define pinPir_1  A1
#define pinPir_2  A2
#define pinHr     A3
#define pinModeSw 8
#define pinCrlServo 9

#define modeRa  0
#define modeVao 1

#define sl_xe_max 4

const int goc_servo[2] = { 0, 120 };

LiquidCrystal_I2C lcd(0X27, 16, 2);

Servo myservo;

bool state_temp_1time_1, state_temp_1time_2, state_temp_1time_3, state_temp_1time_4;
int stateMode_prev = 2;
bool state_read_vao, state_read_ra;
bool state_read_done_vao, state_read_done_ra;
bool state_read_rfid;

bool ttst_1;

bool state_servo_on;

void setup() {
  Serial.begin(9600);

  pinMode(pinHr,    INPUT);
  pinMode(pinPir_1, INPUT);
  pinMode(pinPir_2, INPUT);
  pinMode(pinModeSw,  INPUT);

  myservo.attach(pinServo);
  myservo.write(goc_servo[0]);

  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("TT_HTN - PROJECT");
  lcd.setCursor(0, 1);
  lcd.print(" NHOM 3 CON BAO ");
  delay(2000);
  lcd.clear();

  stateMode_prev = 2;
  state_temp_1time_1 = false; state_temp_1time_2 = false; state_temp_1time_3 = false; state_temp_1time_4 = false;
  state_read_vao = false, state_read_ra = false;
  state_read_done_vao = false, state_read_done_ra = false;
  state_read_rfid = false;

  ttst_1 = false;

  state_servo_on = false;

  Serial.println("__Arduino_start__");
}

void loop() {
  /*
    statePir_1 -> vao
    statePir_2 -> ra
  */
  bool stateHr = digitalRead(pinHr) == 0 ? true : false;
  bool statePir_1 = digitalRead(pinPir_1) == 1 ? true : false;
  bool statePir_2 = digitalRead(pinPir_2) == 1 ? true : false;
  bool stateMode = digitalRead(pinModeSw) == 1 ? modeRa : modeVao;

  bool stateCrlServo = digitalRead(pinCrlServo) == 1 ? true : false;

  if (stateCrlServo == true) {
    if (state_servo_on == false) {
      state_servo_on = true;
      myservo.write(goc_servo[1]);
      reset_all_state();
    }
  }
  else {
    if (state_servo_on == true) {
      state_servo_on = false;
      myservo.write(goc_servo[0]);
      reset_all_state();
    }
  }

  if (stateCrlServo == false) {
    if (stateMode != stateMode_prev) {
        stateMode_prev = stateMode;
        Serial.println("reset all state");
        Serial.println(stateMode == 1 ? "modeVao" : "modeRa");
        reset_all_state();
      }
    if (stateMode == modeVao) {
      // handle some statements about session input gate
      if (state_temp_1time_1 == false) {
        state_temp_1time_1 = true;
        lcd_log(3, "Gui Xe Vao", 4, "Quet The");
      }
      if (statePir_1 == true && state_read_done_vao == false) {
        if (state_temp_1time_2 == false) {
          state_temp_1time_2 = true;
          state_read_vao = true;
          lcd_log(4, "Xin Chao", 2, "Quet The Vao");
          Serial.println("ready_input_gate");
        }
      }
      if (state_read_vao == true) {
        String data = read_data_serial();
        if (data != "NULL") {
          if (state_temp_1time_3 == false) {
            state_temp_1time_3 = true;
            if (data == "duplicate id" || data == "full slot") {
              lcd_log(2, "That bai", 0, data);
              Serial.println("ready_input_gate_fail");
              myservo.write(goc_servo[0]); // servo off
              state_read_done_vao = false;
              state_read_done_ra  = false;
              delay(2000);
              reset_all_state();
            }
            else {
              lcd_log(2, "Da xac nhan", 0, data);
              Serial.println("ready_input_gate_done");
              myservo.write(goc_servo[1]); // servo on
              state_read_done_vao = true;
              state_read_done_ra  = false;
            }
            if(data == "reset all state"){
              reset_all_state();
              }
          }
        }
      }
      if (state_read_done_vao == true) {
        if (stateHr == true) {
          myservo.write(goc_servo[0]);
          reset_all_state();
        }
      }
    }
    else {
      // handle some statements about session output gate
      if (state_temp_1time_1 == false) {
        state_temp_1time_1 = true;
        lcd_log(3, "Lay Xe Ve", 4, "Quet The");
        Serial.println("ready_output_gate");
      }
      if (statePir_2 == true && state_read_done_ra == false) {
        if (state_temp_1time_2 == false) {
          state_temp_1time_2 = true;
          state_read_ra  = true;
          lcd_log(4, "Xin Chao", 2, "Quet The Ra");
          Serial.println("ready_output_gate");
        }
      }
      if (state_read_ra == true) {
        String data = read_data_serial();
        if (data != "NULL") {
          if (state_temp_1time_3 == false) {
            state_temp_1time_3 = true;
            if (data == "No Found Id") {
              lcd_log(2, "That bai", 0, data);
              Serial.println("ready_output_gate_fail");
              myservo.write(goc_servo[0]); // servo off
              state_read_done_vao = false;
              state_read_done_ra  = false;
              delay(2000);
              reset_all_state();
            }
            else {
              lcd_log(2, "Da xac nhan", 0, data);
              Serial.println("ready_output_gate_done");
              myservo.write(goc_servo[1]); // servo on
              state_read_done_vao = false;
              state_read_done_ra  = true;
            }
            if(data == "reset all state"){
              reset_all_state();
              }
          }
        }
      }
      if (state_read_done_ra == true) {
        if (stateHr == true) {
          myservo.write(goc_servo[0]);
          reset_all_state();
        }
      }
    }
  }
}

void lcd_log(int x1, String dt1, int x2, String dt2) {
  lcd.clear();
  lcd.setCursor(x1, 0); lcd.print(dt1);
  lcd.setCursor(x2, 1); lcd.print(dt2);
}

void reset_all_state() {
  state_temp_1time_1 = false; state_temp_1time_2 = false; state_temp_1time_3 = false; state_temp_1time_4 = false;
  state_read_vao = false, state_read_ra = false;
  state_read_done_vao = false, state_read_done_ra = false;
  state_read_rfid = false;
  Serial.println("reset all state");
}

String read_data_serial() {
  if (Serial.available() > 0) {
    String receivedChar = Serial.readStringUntil('\n');
    return receivedChar;
  }
  return "NULL";
}
