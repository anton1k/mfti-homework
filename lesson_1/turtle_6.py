# Нарисуйте спираль. См. теорию. https://ru.wikipedia.org/wiki/Архимедова_спираль

import time
import turtle
from math import *
turtle.shape('turtle')

for i in range(200):
    t = i / 20 * pi
    x = (5 * t) * cos(t)
    y = (5 * t) * sin(t)
    turtle.goto(x, y)

time.sleep(1)