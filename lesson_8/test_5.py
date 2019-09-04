# Нарисуйте кривую Минковского. Кривая Минковского нулевого порядка - горизонтальный отрезок. Затем на каждом шаге каждый из отрезков заменяется на ломанную, состоящую из 8 звеньев.
import time
import turtle
 
turtle.shape('turtle')
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.speed('fastest')
 
def draw (l ,n):
    if n == 0:
        turtle.forward(l)
        return
    l//=4

    draw(l, n-1)
    turtle.left(90)
    draw(l, n-1)
    turtle.right(90)
    draw(l, n-1)
    turtle.right(90)
    draw(l, n-1)
    draw(l, n-1)
    turtle.left(90)
    draw(l, n-1)
    turtle.left(90)
    draw(l, n-1)
    turtle.right(90)
    draw(l, n-1)
   
 
draw(400, 3)
    

time.sleep(2)