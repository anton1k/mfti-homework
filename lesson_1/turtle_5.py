# Нарисуйте паука с n лапами. Пример n = 12:

import time

import turtle

turtle.shape('turtle')
count = 12
for i in range(count):
    turtle.right(360/count)
    turtle.forward(100)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(100)
    turtle.right(-180)

time.sleep(1)