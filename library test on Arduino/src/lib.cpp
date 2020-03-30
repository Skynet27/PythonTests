#include "Arduino.h"
#include "lib.h"

Morse::Morse(int pin, int t)
{
  pinMode(pin, OUTPUT);
  _pin = pin;
  _t = t;
}

void Morse::SOS()
{
  dot();dot();dot();
  dash();dash();dash();
  dot();dot();dot();
}

void Morse::dot()
{
  digitalWrite(_pin, HIGH);
  delay(_t);
  digitalWrite(_pin, LOW);
  delay(_t);
}

void Morse::dash()
{
  digitalWrite(_pin, HIGH);
  delay(_t*2);
  digitalWrite(_pin, LOW);
  delay(_t*2);
}