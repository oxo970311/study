import serial
import time
import turtle
import random
import math

# 센서값 만큼 거북이가 조금씩 이동하다가, 랜덤한 위치에 장애물(직선)이 만들어지면 피해가는 알고리즘
# 만드는중 ...

# 장애물 위치 리스트
obstacle_point = []
obstacle_point_new = []


# 시작 시점 함수
def set_start_point():
    set_point_x = random.randrange(-50, 50)
    set_point_y = random.randrange(-50, 50)
    return set_point_x, set_point_y


# 장애물 만드는 모듈
def random_obstacle_move(x, y):
    obs_module.goto(x, y)
    new_x_point = random.randrange(-300, 300 + 1)
    new_y_point = random.randrange(-300, 300 + 1)
    obs_module.penup()
    obs_module.goto(new_x_point, new_y_point)
    t.width(5)
    obs_module.pendown()
    obstacle_point_new.append((obs_module.pos()))


# 거북이 이동 / 센서로 받은 값만큼
def turtle_move(move):
    t.penup()
    t.forward(move)
    t.pendown()


# 난수로 좌 / 우 선택
def rotate_by_angle(angle):
    if angle == 0:
        t.lt(90)
    else:
        t.rt(90)


# 유클리디안 거리 공식
def distance(x1, x2, y1, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# 거북이 후진
def sensor():
    t.bk(20)

# 난수
rand = random.randrange(1, 360 + 1)
set_point_x = random.randrange(-50, 50)
set_point_y = random.randrange(-50, 50)

# s = turtle.getscreen()
# 거북이, 장애물 모듈 객체 생성
t = turtle.Turtle()
obs_module = turtle.Turtle('circle')
obs_module.shapesize(stretch_wid=0.1, stretch_len=0.1)
t.shape('turtle')
count = 1

# 시작 위치 지정 / 거북이 and 장애물 모듈
obs_module.penup()
obs_module.goto(set_start_point())
obs_module.pendown()
t.penup()
t.goto(set_start_point())
t.pendown()

arduino = serial.Serial('COM5', 9600)
time.sleep(2)

# 메인 코드
try:
    while True:
        angle = random.randrange(0, 2)
        x_point = random.randrange(-300, 300 + 1)
        y_point = random.randrange(-300, 300 + 1)
        if arduino.in_waiting:
            data = arduino.readline().decode('utf-8').strip()
            print("받은 거리 값:", data)
            n_data = data.replace("Distance:", "").strip()
            forward = float(n_data)
            rotate_by_angle(angle)
            turtle_move(forward)
            count += 1
            if count % 10 == 0:
                obstacle_point.append(obs_module.pos())
                random_obstacle_move(x_point, y_point)
                if count > 20:
                    break
                for (x1, y1), (x2, y2) in zip(obstacle_point, obstacle_point_new):
                    print(x1, y1)
                    print(x2, y2)
                    distance_value = distance(x1, x2, y1, y2)
                    print("이동 거리 : ", distance_value)

except KeyboardInterrupt:
    print("종료됨")
finally:
    arduino.close()

turtle.done()

# 출력
print("장애물 현재 위치 : ", obstacle_point)
print("장애물 이동 위치 : ", obstacle_point_new)
