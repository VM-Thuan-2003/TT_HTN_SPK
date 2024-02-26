/*
   Reading the distance with a ping sensor(ultrasonic sensor)
   by Okpaluba Chibuike <chibuikepraise@gmail.com>

   modified on the 29 Oct 2015
   by Okpaluba Chibuike
   <chibuikepraise@gmail.com>S
 */
 
#include <Ultrasonic.h>

const int trigPin1 = 7;
const int echoPin1 = 8;
String unit = "mm";

Ultrasonic ultrasonicSensor1(trigPin1, echoPin1, unit);

void setup()
{
  Serial.begin(9600);
}

void loop() {
//  Serial.print("The Distance is : ");
  Serial.println(ultrasonicSensor1.getDistance());
//  Serial.println(" mm");
}
