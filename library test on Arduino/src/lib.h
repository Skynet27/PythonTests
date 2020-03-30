#ifndef Morse_h
#define Morse_h

#include "Arduino.h"

class Morse
{
  public:
    Morse(int pin, int t);
    void dot();
    void dash();
    void SOS();
  private:
    int _pin;
    int _t;
};

#endif