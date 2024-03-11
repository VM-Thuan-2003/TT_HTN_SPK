#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>

#define pin_hr    A1
#define pin_servo A2
#define pin_pir_1 A3
#define pin_pir_2 A4

const int goc_servo[2] = {0,90};

LiquidCrystal_I2C lcd(0X27, 16, 2);

Servo myservo; 

bool state_read_data_uart = false;

void state_all_reset(){
  state_read_data_uart = false;
}

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
  bool state_hr    = digitalRead(pin_hr)    == 1 ? true : false;
  bool state_pir_1 = digitalRead(pin_pir_1) == 1 ? true : false;
  bool state_pir_2 = digitalRead(pin_pir_2) == 1 ? true : false;


  
  if (Serial.available() > 0) {
    // Read the incoming data and print it to the Serial Monitor
    String receivedChar = Serial.readStringUntil('\n');
    if(receivedChar == "__rasp_start__")
      Serial.println("__rasp_start__");
    else
      Serial.println("__rasp_start__");
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(receivedChar);
  }

}
