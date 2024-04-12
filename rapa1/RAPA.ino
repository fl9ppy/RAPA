// Include necessary libraries
#include <Arduino.h>

// Define pins for motor control
const int leftMotorPin1 = 5;
const int leftMotorPin2 = 4;
const int rightMotorPin1 = 3;
const int rightMotorPin2 = 2;

// Define pins for ultrasonic sensor
const int trigPin = 6;
const int echoPin = 7;

// Define pins for second sensor
const int secondSensorPin = 8;

// Define maximum distance for ultrasonic sensor (in cm)
const int maxDistance = 10;

// Define motor speeds
const int motorSpeed = 150;

void setup() {
  // Initialize serial communication for debugging
  Serial.begin(9600);

  // Initialize motor control pins
  pinMode(leftMotorPin1, OUTPUT);
  pinMode(leftMotorPin2, OUTPUT);
  pinMode(rightMotorPin1, OUTPUT);
  pinMode(rightMotorPin2, OUTPUT);

  // Initialize ultrasonic sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Initialize second sensor pin
  pinMode(secondSensorPin, INPUT);
}

void loop() {
  // Read distance from ultrasonic sensor
  long duration, distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;

  // Read value from second sensor
  int secondSensorValue = digitalRead(secondSensorPin);

  // Debugging output
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.print(" cm, Second Sensor: ");
  Serial.println(secondSensorValue);

  // Check conditions and control motors accordingly
  if (distance <= maxDistance && secondSensorValue == LOW) {
    // Move forward
    digitalWrite(leftMotorPin1, HIGH);
    digitalWrite(leftMotorPin2, LOW);
    digitalWrite(rightMotorPin1, HIGH);
    digitalWrite(rightMotorPin2, LOW);
  } else if (distance <= maxDistance && secondSensorValue == HIGH) {
    // Turn left
    digitalWrite(leftMotorPin1, HIGH);
    digitalWrite(leftMotorPin2, LOW);
    digitalWrite(rightMotorPin1, LOW);
    digitalWrite(rightMotorPin2, HIGH);
    delay(1000); // Adjust delay for desired turn duration
  } else {
    // Stop
    digitalWrite(leftMotorPin1, LOW);
    digitalWrite(leftMotorPin2, LOW);
    digitalWrite(rightMotorPin1, LOW);
    digitalWrite(rightMotorPin2, LOW);
  }

  // Add a delay to control the loop rate
  delay(100);
}
