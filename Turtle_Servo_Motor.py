import serial
import turtle
import random
import math
import time

# 버튼을 안누르면 전진, 누르고 있으면 멈춤
t = turtle.Turtle()
t.shape('turtle')

last_was_180 = False
step = 0

ser = serial.Serial('COM5', 9600)
time.sleep(2)  # 연결 안정화 대기

try:
    while True:
        if ser.in_waiting > 0:
            angle = ser.readline().decode('utf-8').strip()
            # print(f"서보 각도: {angle}")
            int_angle = int(angle)
            if int_angle == 180:
                if not last_was_180:
                    step += 1
                    t.forward(50)
                    print("거북이 %d 발짜국 전진" % step)
                    last_was_180 = True
                    if step == 5:
                        break

            else:
                last_was_180 = False

except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    ser.close()

# turtle.done

# Arduino Code
'''
#include <Servo.h>

Servo myservo;
int pos = 0;
int button = 10;
int buttonState = 0;

void setup() {
  Serial.begin(9600);
  myservo.attach(7);
  pinMode(button, INPUT);
}

void loop() {
buttonState = digitalRead(button);
if (buttonState == HIGH) {
    for (pos = 0; pos <= 180; pos++) {
    myservo.write(pos);
    Serial.println(pos);
    delay(15);
  }

    for (pos = 180; pos >= 0; pos--) {
    myservo.write(pos);
    Serial.println(pos);
    delay(15);
    }
  }
}
'''