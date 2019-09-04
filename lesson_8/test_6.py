# Нарисуйте кривую Леви. Она получается, если взять половину квадрата вида /\, а затем каждую сторону заменить таким же фрагментом и так далее.

import time
import turtle
 
turtle.shape('turtle')
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.speed('fastest')

instruct = [1, 2, 3, 2, 1]

def draw (n, l=None):
    if not l:
        l = 200 / 2 ** (n/2)
    for i in [1, 2, 3, 2, 1]:
        if i == 2:
            if n == 0:
                turtle.forward(l)
            else:
                draw(n-1, l)
        elif i == 1:
            turtle.left(45)
        elif i == 3:
            turtle.right(90)

draw(15)
    
time.sleep(2)