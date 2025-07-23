import serial
import turtle
import random
import math
import time

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
                    t.forward(100)
                    print("거북이 %d 발짜국 전진" % step)
                    last_was_180 = True
                    if step == 3:
                        break

            else:
                last_was_180 = False

except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    ser.close()

# turtle.done()