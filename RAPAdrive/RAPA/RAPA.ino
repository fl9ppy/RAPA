#include <Arduino.h>

// !!!!PIN DECLARATION MIGHT NEED MODIFICATIONS!!!!

// motor pins declaration
const int leftMotorPin1 = 5;
const int leftMotorPin2 = 4;
const int rightMotorPin1 = 3;
const int rightMotorPin2 = 2;

// sensor pins declaration
const int frontTrigPin = 6;
const int frontEchoPin = 7;
const int rightTrigPin = 8;
const int rightEchoPin = 9;

// !!!DISTANCE IN CM!!!
const int maxDistance = 10;

const int motorSpeed = 150;

void setup() {
  Serial.begin(9600);

  // motor pins
  pinMode(leftMotorPin1, OUTPUT);
  pinMode(leftMotorPin2, OUTPUT);
  pinMode(rightMotorPin1, OUTPUT);
  pinMode(rightMotorPin2, OUTPUT);

  // sensor pins
  pinMode(frontTrigPin, OUTPUT);
  pinMode(frontEchoPin, INPUT);
  pinMode(rightTrigPin, OUTPUT);
  pinMode(rightEchoPin, INPUT);
}

// Robot turns 90 degrees to left
void turnLeft(){
  digitalWrite(leftMotorPin1, LOW);
  digitalWrite(leftMotorPin2, HIGH);
  digitalWrite(rightMotorPin1, HIGH);
  digitalWrite(rightMotorPin2, LOW);
  delay(1000);
}

// Robot turns 90 degrees to right
void turnRight(){
  digitalWrite(leftMotorPin1, HIGH);
  digitalWrite(leftMotorPin2, LOW);
  digitalWrite(rightMotorPin1, LOW);
  digitalWrite(rightMotorPin2, HIGH);
  delay(1000);
}

// Robot accelerates straight forward
void forward(){
  digitalWrite(leftMotorPin1, HIGH);
  digitalWrite(leftMotorPin2, LOW);
  digitalWrite(rightMotorPin1, HIGH);
  digitalWrite(rightMotorPin2, LOW);
}

// Robot stops in place
void stop(){
  digitalWrite(leftMotorPin1, LOW);
  digitalWrite(leftMotorPin2, LOW);
  digitalWrite(rightMotorPin1, LOW);
  digitalWrite(rightMotorPin2, LOW);
}

void loop() {
  long frontDuration, frontDistance;
  long rightDuration, rightDistance;
  
  // Distance to front wall
  digitalWrite(frontTrigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(frontTrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(frontTrigPin, LOW);
  frontDuration = pulseIn(frontEchoPin, HIGH);
  frontDistance = frontDuration * 0.034 / 2;

  // Distance to right wall
  digitalWrite(rightTrigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(rightTrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(rightTrigPin, LOW);
  rightDuration = pulseIn(rightEchoPin, HIGH);
  rightDistance = rightDuration * 0.034 / 2;

  // For debugging purposes xD
  Serial.print("Front Distance: ");
  Serial.print(frontDistance);
  Serial.print(" cm, Right Distance: ");
  Serial.println(rightDistance);

  // Check conditions and control motors accordingly
  if (rightDistance <= maxDistance && frontDistance > maxDistance) {
    // Right sensor detects wall
    forward();
  } else if (frontDistance <= maxDistance && rightDistance > maxDistance) {
    // Front sensor detects wall
    turnRight();
  } else if (frontDistance > maxDistance && rightDistance > maxDistance) {
    // Neither sensor detect
    stop();
  } else if (frontDistance <= maxDistance && rightDistance <= maxDistance) {
    // Both sensors detect walls
    turnLeft();
  }
  
  delay(100);
}


/**
 .d888 888  .d8888b.                             
d88P"  888 d88P  Y88b                            
888    888 888    888                            
888888 888 Y88b. d888 88888b.  88888b.  888  888 
888    888  "Y888P888 888 "88b 888 "88b 888  888 
888    888        888 888  888 888  888 888  888 
888    888 Y88b  d88P 888 d88P 888 d88P Y88b 888 
888    888  "Y8888P"  88888P"  88888P"   "Y88888 
                      888      888           888 
                      888      888      Y8b d88P 
                      888      888       "Y88P"  

   .-') _ ) (`-.        ('-.       .-') _        .-. .-')              
  (  OO) ) ( OO ).    _(  OO)     ( OO ) )       \  ( OO )             
,(_)----. (_/.  \_)-.(,------.,--./ ,--,' ,-.-') ,--. ,--. ,--. ,--.   
|       |  \  `.'  /  |  .---'|   \ |  |\ |  |OO)|  .'   / |  | |  |   
'--.   /    \     /\  |  |    |    \|  | )|  |  \|      /, |  | | .-') 
(_/   /      \   \ | (|  '--. |  .     |/ |  |(_/|     ' _)|  |_|( OO )
 /   /___   .'    \_) |  .--' |  |\    | ,|  |_.'|  .   \  |  | | `-' /
|        | /  .'.  \  |  `---.|  | \   |(_|  |   |  |\   \('  '-'(_.-' 
`--------''--'   '--' `------'`--'  `--'  `--'   `--' '--'  `-----'    
**/