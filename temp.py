const int tempPin = A0;
const int greenPin = 8;
const int orangePin = 9;
const int redPin = 10;
void setup() {
  Serial.begin(9600);
  pinMode(greenPin, OUTPUT);
  pinMode(orangePin, OUTPUT);
  pinMode(redPin, OUTPUT);
}
void loop() {
  int sensorValue = analogRead(tempPin);
  float volt = sensorValue * (5.0 / 1023.0); // analog to voltage
  float tempC = volt * 100.0;                // voltage to celsius
  Serial.print("Temperature: ");
  Serial.print(tempC);
  Serial.println(" C");

// Control LED based on temperature
  if (tempC < 40) {
    digitalWrite(greenPin, HIGH);
    digitalWrite(orangePin, LOW);
    digitalWrite(redPin, LOW);
  }
  else if (tempC >= 41 && tempC <= 50) {
    digitalWrite(greenPin, LOW);
    digitalWrite(orangePin, HIGH);
    digitalWrite(redPin, LOW);
  }
  else if (tempC > 50) {
    digitalWrite(greenPin, LOW);
    digitalWrite(orangePin, LOW);
    digitalWrite(redPin, HIGH);
  }
  delay(3000);
}


-----------------------------------------------------------

const int tempPin = A0;

const int greenPin = 8;
const int bluePin = 9;
const int redPin = 10;

void setup()
{
  Serial.begin(9600);

  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(redPin, OUTPUT);
}

void loop()
{
  int sensor_value = analogRead(tempPin);

  float voltage = sensor_value * (5.0 / 1023.0);
  float tempC = voltage * 100.0;

  Serial.print("Temperature: ");
  Serial.print(tempC);
  Serial.println(" C");

  if (tempC < 40)
  {
    digitalWrite(greenPin, 255);
    digitalWrite(bluePin, 0);
    digitalWrite(redPin, 0);
  }
  else if (tempC >= 40 && tempC <= 50)
  {
    digitalWrite(greenPin, 165);
    digitalWrite(bluePin, 0);
    digitalWrite(redPin, 255);
  }
  else
  {
    digitalWrite(greenPin, 0);
    digitalWrite(bluePin, 0);
    digitalWrite(redPin, 255);
  }

  delay(500);
}

----------------------------------------------------------------

const int segments[10][8] = {
  // Digit 0: a, b, c, d, e, f on; g, h off
  {HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, LOW,  LOW},

  // Digit 1: b, c on; others off
  {LOW,  HIGH, HIGH, LOW,  LOW,  LOW,  LOW,  LOW},

  // Digit 2: a, b, d, e, g on
  {HIGH, HIGH, LOW,  HIGH, HIGH, LOW,  HIGH, LOW},

  // Digit 3: a, b, c, d, g on
  {HIGH, HIGH, HIGH, HIGH, LOW,  LOW,  HIGH, LOW},

  // Digit 4: b, c, f, g on
  {LOW,  HIGH, HIGH, LOW,  LOW,  HIGH, HIGH, LOW},

  // Digit 5: a, c, d, f, g on
  {HIGH, LOW,  HIGH, HIGH, LOW,  HIGH, HIGH, LOW},

  // Digit 6: a, c, d, e, f, g on
  {HIGH, LOW,  HIGH, HIGH, HIGH, HIGH, HIGH, LOW},

  // Digit 7: a, b, c on
  {HIGH, HIGH, HIGH, LOW,  LOW,  LOW,  LOW,  LOW},

  // Digit 8: all segments on
  {HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, LOW},

  // Digit 9: a, b, c, d, f, g on
  {HIGH, HIGH, HIGH, HIGH, LOW,  HIGH, HIGH, LOW}
};

const int A = 11;
const int B = 10;
const int C = 7;
const int D = 8;
const int E = 9;
const int F = 12;
const int G = 13;
const int H = 6;

void setup() {
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(C, OUTPUT);
  pinMode(D, OUTPUT);
  pinMode(E, OUTPUT);
  pinMode(F, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(H, OUTPUT);
}

void loop() {
  for (int n = 0; n < 10; n++) {
    digitalWrite(A, segments[n][0]);
    digitalWrite(B, segments[n][1]);
    digitalWrite(C, segments[n][2]);
    digitalWrite(D, segments[n][3]);
    digitalWrite(E, segments[n][4]);
    digitalWrite(F, segments[n][5]);
    digitalWrite(G, segments[n][6]);
    digitalWrite(H, segments[n][7]);
    delay(1000);
  }
}

-------------------------------------------------------------

int led = 13;

String morse[] = {
  ".-",     // A
  "-...",   // B
  "-.-.",   // C
  "-..",   // D
  ".",      // E
  "..-.",   // F
  "--.",    // G
  "....",   // H
  "..",     // I
  ".---",   // J
  "-.-",    // K
  ".-..",   // L
  "--",     // M
  "-.",     // N
  "---",    // O
  ".--.",   // P
  "--.-",   // Q
  ".-.",    // R
  "...",    // S
  "-",      // T
  "..-",    // U
  "...-",   // V
  ".--",    // W
  "-..-",   // X
  "-.--",   // Y
  "--.."    // Z
};


void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);

  Serial.println("Enter message:");
}


void loop() {

  if (Serial.available()) {

    String text = Serial.readString();
    text.toUpperCase();

    Serial.print("Morse: ");

    convertToMorse(text);

  }
}

void convertToMorse(String text) {

  for (int i = 0; i < text.length(); i++) {

    char ch = text[i];

    if (ch == ' ') {
      Serial.print("   ");
      delay(2000);
    }

    else if (ch >= 'A' && ch <= 'Z') {

      String code = morse[ch - 'A'];

      Serial.print(code);
      Serial.print(" ");

      blinkMorse(code);

      delay(1000);  
    }
  }

  Serial.println();
}

void blinkMorse(String code) {

  for (int i = 0; i < code.length(); i++) {

    if (code[i] == '.') {
      dot();
    }

    else if (code[i] == '-') {
      dash();
    }

    delay(500);
  }
}

void dot() {

  digitalWrite(led, HIGH);
  delay(1000);

  digitalWrite(led, LOW);
}

void dash() {

  digitalWrite(led, HIGH);
  delay(3000);

  digitalWrite(led, LOW);
}

-------------------------------------------------------

#include <Servo.h>

const int pirPin = 2;
const int ledPin = 13;
const int servoPin = 9;

Servo myServo;

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);

  myServo.attach(servoPin);
  myServo.write(0);       // Start at 0 degrees

  Serial.begin(9600);

  delay(10000);           // PIR warm-up
}

void loop() {

  int motionDetected = digitalRead(pirPin);

  if (motionDetected == HIGH) {

    Serial.println("Motion detected!");

    // Move to 90 degrees
    myServo.write(90);
    digitalWrite(ledPin, HIGH);

    // Stay at 90 for 2 seconds
    delay(10000);

    // IMPORTANT: return to 0 degrees
    myServo.write(0);
    digitalWrite(ledPin, LOW);

    // Wait until PIR goes LOW before allowing another trigger
    while (digitalRead(pirPin) == HIGH) {
      delay(50);
    }

    Serial.println("Servo returned to 0 degrees.");
  }

  delay(50);
}


---------------------------------------------------------------

#include <Servo.h>

Servo myServo;

int bluePin = 6;
int redPin = 5;
int greenPin = 4;
int buzzerPin = 2;
int sensorPin = 7;
int servoPin = 3;

void setup() {
  pinMode(buzzerPin, OUTPUT);
  pinMode(redPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  myServo.attach(servoPin);
  Serial.begin(9600);
}

void loop() {
  // 1. Send the ultrasonic trigger pulse
  pinMode(sensorPin, OUTPUT);
  digitalWrite(sensorPin, LOW);
  delayMicroseconds(2);
  digitalWrite(sensorPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(sensorPin, LOW);

  // 2. Measure the echo return pulse
  pinMode(sensorPin, INPUT);
  long duration = pulseIn(sensorPin, HIGH);
  float cm = 0.01723 * duration;
  float inch = cm / 2.54;

  // Print distance to Serial Monitor for live verification
  Serial.print("Distance: ");
  Serial.print(cm);
  Serial.println(" cm");

  // 3. Control logic based on distance
  if (cm >= 250) {
    digitalWrite(greenPin, HIGH);
    digitalWrite(redPin, LOW);
    digitalWrite(bluePin, LOW);
    myServo.write(0);
    digitalWrite(buzzerPin, LOW);
  }
  else if (cm < 250 && cm >= 100) {
    digitalWrite(greenPin, LOW);
    digitalWrite(redPin, HIGH);
    digitalWrite(bluePin, LOW);
    myServo.write(0);
    digitalWrite(buzzerPin, LOW);
  }
  else if (cm < 100 && cm > 0) {
    digitalWrite(greenPin, LOW);
    digitalWrite(redPin, LOW);
    digitalWrite(bluePin, HIGH);
    myServo.write(90);
    digitalWrite(buzzerPin, LOW);
  }
  else {
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, LOW);
    digitalWrite(redPin, LOW);
    myServo.write(0);
    digitalWrite(buzzerPin, LOW);
  }

  delay(100);
}


------------------------------------------------------------

#include <LiquidCrystal.h>
#include <Servo.h>

const int moisturePin = A5;
const int redLED = 8;
const int blueLED = 9;
const int greenLED = 13;
const int buzzerPin = 10;
const int buttonPin = A0;
const int servoPin = 7;

Servo myservo;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int contrast = 150;

void setup() {
  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(buzzerPin, OUTPUT);
  
  myservo.attach(servoPin);
  myservo.write(0);
  
  //analogWrite(6, contrast); // Controls LCD contrast on Pin V0
  lcd.begin(16, 2);
}

void loop() {
  int moisture = analogRead(moisturePin);

  lcd.setCursor(0, 0);
  lcd.print("Moisture : ");
  lcd.print(moisture);
  lcd.print("   "); // Clears trailing digits when values change

  if (moisture < 300) {
    myservo.write(0);
    digitalWrite(redLED, HIGH);
    digitalWrite(greenLED, LOW);
    digitalWrite(blueLED, LOW);
    tone(buzzerPin, 1000);
    lcd.setCursor(0, 1);
    lcd.print("Status: Low    ");

    if (digitalRead(buttonPin) == LOW) {
      myservo.write(180);
      noTone(buzzerPin);
      delay(2000);
    }
  } 
  else if (moisture >= 300 && moisture < 700) {
    digitalWrite(redLED, LOW);
    digitalWrite(blueLED, HIGH);
    digitalWrite(greenLED, LOW);
    myservo.write(45);
    noTone(buzzerPin);
    lcd.setCursor(0, 1);
    lcd.print("Status: Medium ");
  } 
  else {
    myservo.write(0);
    digitalWrite(redLED, LOW);
    digitalWrite(blueLED, LOW);
    digitalWrite(greenLED, HIGH);
    noTone(buzzerPin);
    lcd.setCursor(0, 1);
    lcd.print("Status: High   ");
  }

  delay(100);
}


------------------------------------------------------------------


#include <LiquidCrystal.h>
#include <Keypad.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const byte ROWS = 4, COLS = 4;
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte rowPins[ROWS] = {10, 9, 8, 7};
byte colPins[COLS] = {6, A1, A2, A3};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

String pin = "";
const String correctPin = "1234";
int attempts = 3;
const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  lcd.begin(16, 2);
  lcd.print("Enter PIN:");
}

void loop() {
  char key = keypad.getKey();

  if (!key) return;

  if (key == '*') {
    pin = "";
    lcd.clear();
    lcd.print("Enter PIN:");
  }
  else if (key == '#') {
    if (pin == correctPin) {
      lcd.clear();
      lcd.print("Access Granted!");
      lcd.setCursor(0, 1);
      lcd.print("Door Unlocked");
      digitalWrite(ledPin, HIGH);
      delay(4000);
      digitalWrite(ledPin, LOW);
      attempts = 3;
    }
    else if (pin.length() > 0) {
      attempts--;
      lcd.print("Wrong PIN!");

      if (attempts == 0) {
        lcd.clear();
        lcd.print("SYSTEM LOCKED!");

        for (int i = 10; i > 0; i--) {
          lcd.setCursor(0, 1);
          lcd.print("Retry in: ");
          lcd.print(i);
          lcd.print("s   ");
          delay(1000);
        }

        attempts = 3;
      }
      else {
        lcd.setCursor(0, 1);
        lcd.print("Attempts left: ");
        lcd.print(attempts);
        delay(2000);
      }
    }

    pin = "";
    lcd.clear();
    lcd.print("Enter PIN:");
  }
  else if (pin.length() < 4 && key >= '0' && key <= '9') {
    pin += key;
    lcd.setCursor(pin.length() - 1, 1);
    lcd.print('*');
  }
}

-----------------------------------------------------------------------


#include <LiquidCrystal.h>
#include <Keypad.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const byte ROWS = 4, COLS = 4;
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte rowPins[ROWS] = {10, 9, 8, 7};
byte colPins[COLS] = {6, A1, A2, A3};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

String pin = "";
const String correctPin = "1234";
int attempts = 3;
const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  lcd.begin(16, 2);
  lcd.print("Enter PIN:");
}

void loop() {
  char key = keypad.getKey();

  if (!key) return;

  if (key == '*') {
    pin = "";
    lcd.clear();
    lcd.print("Enter PIN:");
  }
  else if (key == '#') {
    if (pin == correctPin) {
      lcd.clear();
      lcd.print("Access Granted!");
      lcd.setCursor(0, 1);
      lcd.print("Door Unlocked");
      digitalWrite(ledPin, HIGH);
      delay(4000);
      digitalWrite(ledPin, LOW);
      attempts = 3;
    }
    else if (pin.length() > 0) {
      attempts--;
      lcd.print("Wrong PIN!");

      if (attempts == 0) {
        lcd.clear();
        lcd.print("SYSTEM LOCKED!");

        for (int i = 10; i > 0; i--) {
          lcd.setCursor(0, 1);
          lcd.print("Retry in: ");
          lcd.print(i);
          lcd.print("s   ");
          delay(1000);
        }

        attempts = 3;
      }
      else {
        lcd.setCursor(0, 1);
        lcd.print("Attempts left: ");
        lcd.print(attempts);
        delay(2000);
      }
    }

    pin = "";
    lcd.clear();
    lcd.print("Enter PIN:");
  }
  else if (pin.length() < 4 && key >= '0' && key <= '9') {
    pin += key;
    lcd.setCursor(pin.length() - 1, 1);
    lcd.print('*');
  }
}

-------------------------------------

const int tempPin = A0;
const int greenPin = 8;
const int orangePin = 9;
const int redPin = 10;
void setup() {
  Serial.begin(9600);
  pinMode(greenPin, OUTPUT);
  pinMode(orangePin, OUTPUT);
  pinMode(redPin, OUTPUT);
}
void loop() {
  int sensorValue = analogRead(tempPin);
  float volt = sensorValue * (5.0 / 1023.0); // analog to voltage
  float tempC = volt * 100.0;                // voltage to celsius
  Serial.print("Temperature: ");
  Serial.print(tempC);
  Serial.println(" C");

// Control LED based on temperature
  if (tempC < 40) {
    digitalWrite(greenPin, HIGH);
    digitalWrite(orangePin, LOW);
    digitalWrite(redPin, LOW);
  }
  else if (tempC >= 41 && tempC <= 50) {
    digitalWrite(greenPin, LOW);
    digitalWrite(orangePin, HIGH);
    digitalWrite(redPin, LOW);
  }
  else if (tempC > 50) {
    digitalWrite(greenPin, LOW);
    digitalWrite(orangePin, LOW);
    digitalWrite(redPin, HIGH);
  }
  delay(3000);
}


-----------------------------------------------------------

const int tempPin = A0;

const int greenPin = 8;
const int bluePin = 9;
const int redPin = 10;

void setup()
{
  Serial.begin(9600);

  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(redPin, OUTPUT);
}

void loop()
{
  int sensor_value = analogRead(tempPin);

  float voltage = sensor_value * (5.0 / 1023.0);
  float tempC = voltage * 100.0;

  Serial.print("Temperature: ");
  Serial.print(tempC);
  Serial.println(" C");

  if (tempC < 40)
  {
    digitalWrite(greenPin, 255);
    digitalWrite(bluePin, 0);
    digitalWrite(redPin, 0);
  }
  else if (tempC >= 40 && tempC <= 50)
  {
    digitalWrite(greenPin, 165);
    digitalWrite(bluePin, 0);
    digitalWrite(redPin, 255);
  }
  else
  {
    digitalWrite(greenPin, 0);
    digitalWrite(bluePin, 0);
    digitalWrite(redPin, 255);
  }

  delay(500);
}

----------------------------------------------------------------

const int segments[10][8] = {
  // Digit 0: a, b, c, d, e, f on; g, h off
  {HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, LOW,  LOW},

  // Digit 1: b, c on; others off
  {LOW,  HIGH, HIGH, LOW,  LOW,  LOW,  LOW,  LOW},

  // Digit 2: a, b, d, e, g on
  {HIGH, HIGH, LOW,  HIGH, HIGH, LOW,  HIGH, LOW},

  // Digit 3: a, b, c, d, g on
  {HIGH, HIGH, HIGH, HIGH, LOW,  LOW,  HIGH, LOW},

  // Digit 4: b, c, f, g on
  {LOW,  HIGH, HIGH, LOW,  LOW,  HIGH, HIGH, LOW},

  // Digit 5: a, c, d, f, g on
  {HIGH, LOW,  HIGH, HIGH, LOW,  HIGH, HIGH, LOW},

  // Digit 6: a, c, d, e, f, g on
  {HIGH, LOW,  HIGH, HIGH, HIGH, HIGH, HIGH, LOW},

  // Digit 7: a, b, c on
  {HIGH, HIGH, HIGH, LOW,  LOW,  LOW,  LOW,  LOW},

  // Digit 8: all segments on
  {HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, LOW},

  // Digit 9: a, b, c, d, f, g on
  {HIGH, HIGH, HIGH, HIGH, LOW,  HIGH, HIGH, LOW}
};

const int A = 11;
const int B = 10;
const int C = 7;
const int D = 8;
const int E = 9;
const int F = 12;
const int G = 13;
const int H = 6;

void setup() {
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(C, OUTPUT);
  pinMode(D, OUTPUT);
  pinMode(E, OUTPUT);
  pinMode(F, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(H, OUTPUT);
}

void loop() {
  for (int n = 0; n < 10; n++) {
    digitalWrite(A, segments[n][0]);
    digitalWrite(B, segments[n][1]);
    digitalWrite(C, segments[n][2]);
    digitalWrite(D, segments[n][3]);
    digitalWrite(E, segments[n][4]);
    digitalWrite(F, segments[n][5]);
    digitalWrite(G, segments[n][6]);
    digitalWrite(H, segments[n][7]);
    delay(1000);
  }
}

-------------------------------------------------------------

int led = 13;

String morse[] = {
  ".-",     // A
  "-...",   // B
  "-.-.",   // C
  "-..",   // D
  ".",      // E
  "..-.",   // F
  "--.",    // G
  "....",   // H
  "..",     // I
  ".---",   // J
  "-.-",    // K
  ".-..",   // L
  "--",     // M
  "-.",     // N
  "---",    // O
  ".--.",   // P
  "--.-",   // Q
  ".-.",    // R
  "...",    // S
  "-",      // T
  "..-",    // U
  "...-",   // V
  ".--",    // W
  "-..-",   // X
  "-.--",   // Y
  "--.."    // Z
};


void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);

  Serial.println("Enter message:");
}


void loop() {

  if (Serial.available()) {

    String text = Serial.readString();
    text.toUpperCase();

    Serial.print("Morse: ");

    convertToMorse(text);

  }
}

void convertToMorse(String text) {

  for (int i = 0; i < text.length(); i++) {

    char ch = text[i];

    if (ch == ' ') {
      Serial.print("   ");
      delay(2000);
    }

    else if (ch >= 'A' && ch <= 'Z') {

      String code = morse[ch - 'A'];

      Serial.print(code);
      Serial.print(" ");

      blinkMorse(code);

      delay(1000);  
    }
  }

  Serial.println();
}

void blinkMorse(String code) {

  for (int i = 0; i < code.length(); i++) {

    if (code[i] == '.') {
      dot();
    }

    else if (code[i] == '-') {
      dash();
    }

    delay(500);
  }
}

void dot() {

  digitalWrite(led, HIGH);
  delay(1000);

  digitalWrite(led, LOW);
}

void dash() {

  digitalWrite(led, HIGH);
  delay(3000);

  digitalWrite(led, LOW);
}

-------------------------------------------------------

#include <Servo.h>

const int pirPin = 2;
const int ledPin = 13;
const int servoPin = 9;

Servo myServo;

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);

  myServo.attach(servoPin);
  myServo.write(0);       // Start at 0 degrees

  Serial.begin(9600);

  delay(10000);           // PIR warm-up
}

void loop() {

  int motionDetected = digitalRead(pirPin);

  if (motionDetected == HIGH) {

    Serial.println("Motion detected!");

    // Move to 90 degrees
    myServo.write(90);
    digitalWrite(ledPin, HIGH);

    // Stay at 90 for 2 seconds
    delay(10000);

    // IMPORTANT: return to 0 degrees
    myServo.write(0);
    digitalWrite(ledPin, LOW);

    // Wait until PIR goes LOW before allowing another trigger
    while (digitalRead(pirPin) == HIGH) {
      delay(50);
    }

    Serial.println("Servo returned to 0 degrees.");
  }

  delay(50);
}


---------------------------------------------------------------

#include <Servo.h>

Servo myServo;

int bluePin = 6;
int redPin = 5;
int greenPin = 4;
int buzzerPin = 2;
int sensorPin = 7;
int servoPin = 3;

void setup() {
  pinMode(buzzerPin, OUTPUT);
  pinMode(redPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  myServo.attach(servoPin);
  Serial.begin(9600);
}

void loop() {
  // 1. Send the ultrasonic trigger pulse
  pinMode(sensorPin, OUTPUT);
  digitalWrite(sensorPin, LOW);
  delayMicroseconds(2);
  digitalWrite(sensorPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(sensorPin, LOW);

  // 2. Measure the echo return pulse
  pinMode(sensorPin, INPUT);
  long duration = pulseIn(sensorPin, HIGH);
  float cm = 0.01723 * duration;
  float inch = cm / 2.54;

  // Print distance to Serial Monitor for live verification
  Serial.print("Distance: ");
  Serial.print(cm);
  Serial.println(" cm");

  // 3. Control logic based on distance
  if (cm >= 250) {
    digitalWrite(greenPin, HIGH);
    digitalWrite(redPin, LOW);
    digitalWrite(bluePin, LOW);
    myServo.write(0);
    digitalWrite(buzzerPin, LOW);
  }
  else if (cm < 250 && cm >= 100) {
    digitalWrite(greenPin, LOW);
    digitalWrite(redPin, HIGH);
    digitalWrite(bluePin, LOW);
    myServo.write(0);
    digitalWrite(buzzerPin, LOW);
  }
  else if (cm < 100 && cm > 0) {
    digitalWrite(greenPin, LOW);
    digitalWrite(redPin, LOW);
    digitalWrite(bluePin, HIGH);
    myServo.write(90);
    digitalWrite(buzzerPin, LOW);
  }
  else {
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, LOW);
    digitalWrite(redPin, LOW);
    myServo.write(0);
    digitalWrite(buzzerPin, LOW);
  }

  delay(100);
}


------------------------------------------------------------

#include <LiquidCrystal.h>
#include <Servo.h>

const int moisturePin = A5;
const int redLED = 8;
const int blueLED = 9;
const int greenLED = 13;
const int buzzerPin = 10;
const int buttonPin = A0;
const int servoPin = 7;

Servo myservo;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int contrast = 150;

void setup() {
  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(buzzerPin, OUTPUT);
  
  myservo.attach(servoPin);
  myservo.write(0);
  
  //analogWrite(6, contrast); // Controls LCD contrast on Pin V0
  lcd.begin(16, 2);
}

void loop() {
  int moisture = analogRead(moisturePin);

  lcd.setCursor(0, 0);
  lcd.print("Moisture : ");
  lcd.print(moisture);
  lcd.print("   "); // Clears trailing digits when values change

  if (moisture < 300) {
    myservo.write(0);
    digitalWrite(redLED, HIGH);
    digitalWrite(greenLED, LOW);
    digitalWrite(blueLED, LOW);
    tone(buzzerPin, 1000);
    lcd.setCursor(0, 1);
    lcd.print("Status: Low    ");

    if (digitalRead(buttonPin) == LOW) {
      myservo.write(180);
      noTone(buzzerPin);
      delay(2000);
    }
  } 
  else if (moisture >= 300 && moisture < 700) {
    digitalWrite(redLED, LOW);
    digitalWrite(blueLED, HIGH);
    digitalWrite(greenLED, LOW);
    myservo.write(45);
    noTone(buzzerPin);
    lcd.setCursor(0, 1);
    lcd.print("Status: Medium ");
  } 
  else {
    myservo.write(0);
    digitalWrite(redLED, LOW);
    digitalWrite(blueLED, LOW);
    digitalWrite(greenLED, HIGH);
    noTone(buzzerPin);
    lcd.setCursor(0, 1);
    lcd.print("Status: High   ");
  }

  delay(100);
}


------------------------------------------------------------------


#include <LiquidCrystal.h>
#include <Keypad.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const byte ROWS = 4, COLS = 4;
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte rowPins[ROWS] = {10, 9, 8, 7};
byte colPins[COLS] = {6, A1, A2, A3};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

String pin = "";
const String correctPin = "1234";
int attempts = 3;
const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  lcd.begin(16, 2);
  lcd.print("Enter PIN:");
}

void loop() {
  char key = keypad.getKey();

  if (!key) return;

  if (key == '*') {
    pin = "";
    lcd.clear();
    lcd.print("Enter PIN:");
  }
  else if (key == '#') {
    if (pin == correctPin) {
      lcd.clear();
      lcd.print("Access Granted!");
      lcd.setCursor(0, 1);
      lcd.print("Door Unlocked");
      digitalWrite(ledPin, HIGH);
      delay(4000);
      digitalWrite(ledPin, LOW);
      attempts = 3;
    }
    else if (pin.length() > 0) {
      attempts--;
      lcd.print("Wrong PIN!");

      if (attempts == 0) {
        lcd.clear();
        lcd.print("SYSTEM LOCKED!");

        for (int i = 10; i > 0; i--) {
          lcd.setCursor(0, 1);
          lcd.print("Retry in: ");
          lcd.print(i);
          lcd.print("s   ");
          delay(1000);
        }

        attempts = 3;
      }
      else {
        lcd.setCursor(0, 1);
        lcd.print("Attempts left: ");
        lcd.print(attempts);
        delay(2000);
      }
    }

    pin = "";
    lcd.clear();
    lcd.print("Enter PIN:");
  }
  else if (pin.length() < 4 && key >= '0' && key <= '9') {
    pin += key;
    lcd.setCursor(pin.length() - 1, 1);
    lcd.print('*');
  }
}


----------------------------------------------------------------

const int buzzerPin = 9;
const unsigned long interval = 15000;

unsigned long startTime;
bool timeStarted = false;

void setup() {
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);

  startTime = millis();
  timeStarted = true;
}

void loop() {
  if (timeStarted) {
    unsigned long currentMillis = millis();
    unsigned long elapsedTime = currentMillis - startTime;

    if (elapsedTime >= interval) {
      tone(buzzerPin, 1000);      // 1000 Hz tone
      delay(2000);                // Play for 2 seconds
      noTone(buzzerPin);

      timeStarted = false;
      Serial.println("Time's up!");
    }
  }
}

---------------------------------------------------------------------

int Relay = 2;

void setup() {
  pinMode(Relay, INPUT);
  Serial.begin(9600);
}

void loop() {
  int Relay_1 = digitalRead(Relay);
  
  if (Relay_1) {
    Serial.println("Button On");
    delay(1000);
  } else {
    Serial.println("Button Off");
    delay(1000);
  }
}

---------------------------------------------------------------------

const int photoPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int photoValue = analogRead(photoPin);

  Serial.print("Light level: ");
  Serial.println(photoValue);

  delay(1000);
}

---------------------------------------------------------------

int LEDPin = 8;
int BUTTONPin = 13;
int BUTTONSTATE = 0;

void setup() {
  pinMode(LEDPin, OUTPUT);
  pinMode(BUTTONPin, INPUT);
}

void loop() {
  BUTTONSTATE = digitalRead(BUTTONPin);

  if (BUTTONSTATE == HIGH) {
    digitalWrite(LEDPin, HIGH);
  } else {
    digitalWrite(LEDPin, LOW);
  }
}

---------------------------------------------------------------------

#include <LiquidCrystal.h>

// Initialize the library with LCD interface pins:
// LiquidCrystal(rs, enable, d4, d5, d6, d7)
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

// Pin definition for TMP36 sensor
const int tempSensorPin = A0;

void setup() {
  // Set up the LCDs number of columns and rows:
  lcd.begin(16, 2);
  
  // Print static heading on line 1
  lcd.setCursor(0, 0);
  lcd.print("Temp Monitor");
}

void loop() {
  // Read analog value (0 - 1023)
  int rawVal = analogRead(tempSensorPin);
  
  // Convert reading to voltage (0V - 5V)
  float voltage = rawVal * (5.0 / 1023.0);
  
  // Convert voltage to Celsius (TMP36: 500mV offset, 10mV/°C)
  float tempC = (voltage - 0.5) * 100.0;

  // Set cursor to second line (row 1)
  lcd.setCursor(0, 1);
  
  // Display output
  lcd.print("Temp: ");
  lcd.print(tempC, 1);
  lcd.print(" C   ");

  delay(1000);
}
