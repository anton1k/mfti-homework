# Нарисуйте 10 вложенных квадратов.

import time

import turtle

step = 10
turtle.shape('turtle')
for i in range(10):
    turtle.penup()	
    turtle.left(-90)
    turtle.forward(10)
    turtle.left(-90)
    turtle.forward(10)
    turtle.left(180)
    turtle.pendown()

    for j in range(4):
        turtle.forward(step)
        turtle.left(90)

    step += 20

time.sleep(1)