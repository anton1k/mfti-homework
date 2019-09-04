# Нарисуйте две звезды: одну с 5 вершинами, другую — с 11. Используйте функцию, рисующую звезду с n вершинами.
import time
from turtle import Turtle
from threading import Thread

def star(n, d, x):
    turtle = Turtle()
    turtle.shape('turtle')
    q = 180 / n
    turtle.penup()
    turtle.setx(x)
    turtle.pendown()
    turtle.left(180)
    for _ in range(n):
        turtle.forward(d)
        turtle.left(180 - q)


Thread(target = star(5, 150, -100)).start()
Thread(target = star(11, 150, 100)).start()
    
    
time.sleep(2)

