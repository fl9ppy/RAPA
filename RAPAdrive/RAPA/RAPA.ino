// Include necessary libraries
#include <Arduino.h>

// Define pins for motor control
const int leftMotorPin1 = 5;
const int leftMotorPin2 = 4;
const int rightMotorPin1 = 3;
const int rightMotorPin2 = 2;

// Define pins for ultrasonic sensors
const int frontTrigPin = 6;
const int frontEchoPin = 7;
const int rightTrigPin = 8;
const int rightEchoPin = 9;

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
  pinMode(frontTrigPin, OUTPUT);
  pinMode(frontEchoPin, INPUT);
  pinMode(rightTrigPin, OUTPUT);
  pinMode(rightEchoPin, INPUT);
}

void loop() {
  // Read distance from ultrasonic sensors
  long frontDuration, frontDistance;
  long rightDuration, rightDistance;
  
  // Read distance from front ultrasonic sensor
  digitalWrite(frontTrigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(frontTrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(frontTrigPin, LOW);
  frontDuration = pulseIn(frontEchoPin, HIGH);
  frontDistance = frontDuration * 0.034 / 2;

  // Read distance from right ultrasonic sensor
  digitalWrite(rightTrigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(rightTrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(rightTrigPin, LOW);
  rightDuration = pulseIn(rightEchoPin, HIGH);
  rightDistance = rightDuration * 0.034 / 2;

  // Debugging output
  Serial.print("Front Distance: ");
  Serial.print(frontDistance);
  Serial.print(" cm, Right Distance: ");
  Serial.println(rightDistance);

  // Check conditions and control motors accordingly
  if (rightDistance <= maxDistance && frontDistance > maxDistance) {
    // Case 1: Only right sensor detects a wall, go straight forward
    digitalWrite(leftMotorPin1, HIGH);
    digitalWrite(leftMotorPin2, LOW);
    digitalWrite(rightMotorPin1, HIGH);
    digitalWrite(rightMotorPin2, LOW);
  } else if (frontDistance <= maxDistance && rightDistance > maxDistance) {
    // Case 2: Front sensor detects a wall, rotate 90 degrees right
    digitalWrite(leftMotorPin1, HIGH);
    digitalWrite(leftMotorPin2, LOW);
    digitalWrite(rightMotorPin1, LOW);
    digitalWrite(rightMotorPin2, HIGH);
    delay(1000); // Adjust delay for desired turn duration
  } else if (frontDistance > maxDistance && rightDistance > maxDistance) {
    // Case 3: Both sensors don't detect any wall, stop motors
    digitalWrite(leftMotorPin1, LOW);
    digitalWrite(leftMotorPin2, LOW);
    digitalWrite(rightMotorPin1, LOW);
    digitalWrite(rightMotorPin2, LOW);
  } else if (frontDistance <= maxDistance && rightDistance <= maxDistance) {
    // Case 4: Both sensors detect walls, rotate 90 degrees left
    digitalWrite(leftMotorPin1, LOW);
    digitalWrite(leftMotorPin2, HIGH);
    digitalWrite(rightMotorPin1, HIGH);
    digitalWrite(rightMotorPin2, LOW);
    delay(1000); // Adjust delay for desired turn duration
  }

  // Add a delay to control the loop rate
  delay(100);
}
