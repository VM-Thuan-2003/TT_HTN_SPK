#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>

#define pin_hr 10
#define pin_servo 9
#define pin_pir_1 11
#define pin_pir_2 12

const int goc_servo[2] = {0,90};

LiquidCrystal_I2C lcd(0X27, 16, 2);

Servo myservo; 

void setup() {
  Serial.begin(9600);
  
  pinMode(pin_hr, INPUT);
  pinMode(pin_pir_1, INPUT);
  pinMode(pin_pir_2, INPUT);
  
  myservo.attach(pin_servo);
  myservo.write(goc_servo[0]);

  lcd.init();
  lcd.backlight();
}

void loop() {
  lcd.setCursor(2, 0);
  lcd.print("DIEN TU DAT");
  lcd.setCursor(0, 1);
  lcd.print("Bai Test LCD I2C ");
  // delay(100);
  int state_hr = digitalRead(pin_hr);
  int state_pir_1 = digitalRead(pin_pir_1);
  int state_pir_2= digitalRead(pin_pir_2);

  Serial.print("state_hr: "); Serial.print(state_hr); Serial.print(" ");
  Serial.print("state_pir_1: "); Serial.print(state_pir_1); Serial.print(" ");
  Serial.print("state_pir_2: "); Serial.print(state_pir_2); Serial.println(" ");
  
  myservo.write(goc_servo[1]);

}