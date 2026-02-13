#include <SoftwareSerial.h>

// Bluetooth on pins 10 (RX) and 11 (TX)
SoftwareSerial BT(10, 11);  

// Define motor pins
#define motorA1 7 // IN1
#define motorA2 6 // IN2
#define motorB1 5 // IN3
#define motorB2 4 // IN4
#define ENA 9     // PWM for motor A (use pin 9)
#define ENB 3     // PWM for motor B (use pin 3)

void setup() {
  Serial.begin(9600);   // Serial Monitor
  BT.begin(9600);       // Bluetooth communication
  pinMode(motorA1, OUTPUT);
  pinMode(motorA2, OUTPUT);
  pinMode(motorB1, OUTPUT);
  pinMode(motorB2, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
}

void loop() {
  if (BT.available()) {
    char command = BT.read(); // Read command from Bluetooth
    Serial.println(command);  // Debugging on Serial Monitor
    controlMotors(command);
  }
}

void controlMotors(char command) {
  switch (command) {
    case 'F': // Move Forward
      digitalWrite(motorA1, LOW);
      digitalWrite(motorA2, HIGH);
      digitalWrite(motorB1, HIGH);
      digitalWrite(motorB2, LOW);
      analogWrite(ENA, 255);
      analogWrite(ENB, 255);
      break;

    case 'B': // Move Backward
      digitalWrite(motorA1, HIGH);
      digitalWrite(motorA2, LOW);
      digitalWrite(motorB1, LOW);
      digitalWrite(motorB2, HIGH);
      analogWrite(ENA, 255);
      analogWrite(ENB, 255);
      break;

    case 'L': // Turn Left
      digitalWrite(motorA1, LOW);
      digitalWrite(motorA2, HIGH);
      digitalWrite(motorB1, LOW);
      digitalWrite(motorB2, HIGH);
      analogWrite(ENA, 255);
      analogWrite(ENB, 255);
      break;

    case 'R': // Turn Right
      digitalWrite(motorA1, HIGH);
      digitalWrite(motorA2, LOW);
      digitalWrite(motorB1, HIGH);
      digitalWrite(motorB2, LOW);
      analogWrite(ENA, 255);
      analogWrite(ENB, 255);
      break;

    case 'S': // Stop
      digitalWrite(motorA1, LOW);
      digitalWrite(motorA2, LOW);
      digitalWrite(motorB1, LOW);
      digitalWrite(motorB2, LOW);
      break;

    default:
      break;
  }
}