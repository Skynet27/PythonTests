#include <Arduino.h>
#include <FastLED.h>
#include <IRremote.h>

//#include <EEPROM.h>

IRrecv IR(44);
decode_results res;

#define NUM_LEDS 64

#define brgP 0x20DF40BF
#define brgM 0x20DFC03F
#define onORoff 0x20DF22DD

CRGB leds[NUM_LEDS];

byte inputDelay = 50;
byte brgInputDelay = 120;
unsigned int currentMillis;
unsigned int lastMillis;
unsigned int lastMillis1;

boolean ledON;
/*
unsigned int lastCode;
unsigned int newCode;
*/
//boolean onOff = EEPROM.read(0);
byte brg;

void turnLEDsOn();
void turnLEDsOff();
void brgUp();
void brgDown();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.print("Setting up the inputs and the leds...");
  pinMode(52,INPUT_PULLUP);
  pinMode(50,INPUT_PULLUP);
  pinMode(48,INPUT_PULLUP);
  pinMode(46,INPUT_PULLUP);
  IR.enableIRIn();
  brg = 10;
  /*if (brg>70) {
    brg = 20;
    EEPROM.write(2,brg);
  }*/
  FastLED.addLeds<WS2812B,8,GRB>(leds,NUM_LEDS);
  FastLED.setBrightness(brg);
  _delay_ms(100);
  Serial.println("   ok");
  Serial.print("Testing the leds...");
  for (int i = 0; i <= NUM_LEDS; i++) {
    leds[i] = CRGB::White;
    if (i>0)
      leds[i-1] = CRGB::Black;
    FastLED.show();
    _delay_ms(20);
  }
  Serial.println("   ok");
  /*if (onOff==1) {
    for (int i = 0; i<=NUM_LEDS; i++) {
      leds[i].setRGB(255,180,60);
    }
    FastLED.show();
  }*/
  lastMillis = millis();
}

void loop() {

  currentMillis = millis();
  if ((digitalRead(52)==0) && ((currentMillis-lastMillis)>inputDelay)) {
    turnLEDsOn();
  }

  if ((digitalRead(50)==0) && ((currentMillis-lastMillis)>inputDelay)) {
    turnLEDsOff();
  }

  if ((digitalRead(48)==0) && ((currentMillis-lastMillis)>brgInputDelay)) {
    brgUp();
  }

  if ((digitalRead(46)==0) && ((currentMillis-lastMillis)>brgInputDelay)) {
    brgDown();
  }

  /*if ((currentMillis-lastMillis1)>1000) {
    byte val = EEPROM.read(2);
    Serial.print("Value of the EEPROM from address:2 == ");
    Serial.println(val);
    lastMillis1 = millis();
  }*/

  if (IR.decode(&res)) {
    //newCode = res.value;
    IR.resume(); // Receive the next value
    if ((currentMillis - lastMillis1)<200) {  // Másik fajta feltétel: ((lastCode == newCode) && ((currentMillis - lastMillis1)<200)
      Serial.println("Nem lehet ((ugyan azt kétszer)) ilyen rövid időn belül:");
      //lastCode = res.value;
    }else{
      switch (res.value)
      {
      case brgP:
        brgUp();
        break;

      case brgM:
        brgDown();
        break;

      case onORoff:
        if (ledON == 0) {
          turnLEDsOn();
        }else if (ledON == 1) {
          turnLEDsOff();
        }
        break;

      default:
        Serial.print("Nem konfigurált kód: ");
        break;
      }
      
      
      Serial.println(res.value, HEX);
      //lastCode = res.value;
      lastMillis1 = millis();
    }
  }
}

void turnLEDsOff() {
  for (int i = 0; i<=NUM_LEDS-9; i++) {
    leds[i] = CRGB::Black;
    ledON = 0;
    FastLED.show();
  }
  //EEPROM.write(0,1);
  lastMillis = millis();
}

void turnLEDsOn() {
  for (int i = 0; i<=NUM_LEDS-9; i++) {
    leds[i].setRGB(255,160,55);
    //leds[i].setRGB(200,27,0); //index szín
    //leds[i] = CRGB::Red;
    ledON = 1;
    FastLED.show();
  }
  //EEPROM.write(0,1);
  lastMillis = millis();
}

void brgUp() {
  brg +=10;
  if (brg>60)
    brg = 60;
  //EEPROM.write(2,brg);
  FastLED.setBrightness(brg);
  FastLED.show();
  lastMillis = millis();
}

void brgDown() {
  brg -=10;
  if ((brg<10)||(brg>60))
    brg = 10;
  //EEPROM.write(2,brg);
  FastLED.setBrightness(brg);
  FastLED.show();
  lastMillis = millis();
}