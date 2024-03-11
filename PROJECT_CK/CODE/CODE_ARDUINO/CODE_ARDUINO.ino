#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>

#define pin_servo A0
#define pin_hr    A1
#define pin_pir_1 A2
#define pin_pir_2 A3

const int goc_servo[2] = {0,90};

LiquidCrystal_I2C lcd(0X27, 16, 2);

Servo myservo; 

unsigned long prev_time = 0;
int time_delay = 0;

bool state_temp_1 = false;
bool state_temp_2 = false;
bool state_temp_3 = false;

bool state_read_rfid = false;

bool state_read_checkin = false;
bool state_read_checkout = false;

bool state_read_done_checkin = false;
bool state_read_done_checkout = false;

bool state_servo_on = false;

void setup() {
  Serial.begin(9600);
  
  pinMode(pin_hr, INPUT);
  pinMode(pin_pir_1, INPUT);
  pinMode(pin_pir_2, INPUT);
  
  state_all_reset();

  myservo.attach(pin_servo);
  myservo.write(goc_servo[0]);

  lcd.init();
  lcd.backlight();

  lcd.setCursor(0, 0);
  lcd.print("TT_HTN - PROJECT");
  lcd.setCursor(0, 1);
  lcd.print(" NHOM 3 CON BAO ");

  delay(1000);
  lcd.clear();
  
  Serial.println("__Arduino_start__");
}

void loop() {
  /*
    state_pir_1 -> check in
    state_pir_2 -> check out
  */
  bool state_hr    = digitalRead(pin_hr)    == 1 ? true : false;
  bool state_pir_1 = digitalRead(pin_pir_1) == 1 ? true : false;
  bool state_pir_2 = digitalRead(pin_pir_2) == 1 ? true : false;


  if(state_read_rfid == false)
    if(state_read_done_checkin == false && state_read_done_checkout == false){
      
      if(state_pir_1 == true){ // checkin
        if(state_temp_1 == false){
            state_temp_1 = true;
            state_read_checkin = true;
            state_read_checkout = false;
        }
      }
      
      if(state_pir_2 == true){ // checkout
          if(state_temp_2 == false){
              state_temp_2 = true;
              state_read_checkin = false;
              state_read_checkout = true;
          }
      }
    }
    else{
      // statement when state_read_done_checkin == true || state_read_done_checkin == true
      
    }
  else{
      // statement when state_read_rfid == true
      
  }

  if(state_read_checkin == true || state_read_checkout == true){
      if(time_delay <= 20){
        time_delay += delay_1s();
      }
      else{
        time_delay = 0;
        state_all_reset();  
      }
  }

  Serial.print(String(state_hr));                 Serial.print(";");
  Serial.print(String(state_pir_1));              Serial.print(";");
  Serial.print(String(state_pir_2));              Serial.print(";");
  Serial.print(String(state_read_checkin));       Serial.print(";");
  Serial.print(String(state_read_checkout));      Serial.print(";");
  Serial.print(String(state_read_done_checkin));  Serial.print(";");
  Serial.print(String(state_read_done_checkout)); Serial.print(";");
  Serial.print(String(state_read_rfid));          Serial.print(";");
  Serial.print(String(time_delay));               Serial.print(";");
  Serial.println("");
  
}

bool delay_1s(){
  unsigned long curr_time = millis();
  if(curr_time - prev_time >= 1000){
    prev_time = curr_time;
    return true;  
  }
  else return false;
}

void state_all_reset(){
  bool state_temp_1 = false;
  bool state_temp_2 = false;
  bool state_temp_3 = false;
  
  bool state_read_rfid = false;
  
  bool state_read_checkin = false;
  bool state_read_checkout = false;
  
  bool state_read_done_checkin = false;
  bool state_read_done_checkout = false;
}

String read_data_serial(){
    if (Serial.available() > 0){
        String receivedChar = Serial.readStringUntil('\n');
        if(receivedChar == "__rasp_start__")
          Serial.println("__rasp_start__");
          lcd.setCursor(0, 0);
          lcd.print("__rasp_start__");
          delay(2000);
          lcd.clear();
        return receivedChar;
    }
}
