# Нарисуйте «бабочку» из окружностей. Используйте функцию, рисующую окружность.
import time

from turtle import Turtle, Screen

count = 8
screen = Screen()
WIDTH = screen.window_width()

turtle = Turtle(visible=False)

turtle.shape('turtle')

turtle.penup()       
turtle.goto(-WIDTH/2 + 200, 0)
turtle.pendown()

turtle.right(-90) 

for _ in range(count):
    turtle.circle(-50, 180)
    turtle.circle(-10, 180)

time.sleep(1)