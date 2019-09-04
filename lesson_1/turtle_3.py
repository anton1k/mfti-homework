# Нарисуйте окружность. Воспользуйтесь тем фактом, что правильный многоугольник с большим числом сторон будет выглядеть как окружность.

import time

import turtle

turtle.shape('turtle')
for i in range(360):
    turtle.forward(2)
    turtle.left(2)

time.sleep(1)