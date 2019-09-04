# Нарисуйте «квадратную» спираль.

import time
import turtle
from math import *
turtle.shape('turtle')

length = 10
for i in range(20):
    turtle.forward(length)
    turtle.left(90)
    length += 10

time.sleep(1)