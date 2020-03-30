#include <Arduino.h>
#include "lib.h"

Morse led(13,175);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("System is ready.");
}

void loop() {
  // put your main code here, to run repeatedly:
  led.SOS();
  Serial.println();
  delay(2000);
}
