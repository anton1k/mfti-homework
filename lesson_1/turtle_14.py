# Нарисуйте две звезды: одну с 5 вершинами, другую — с 11. Используйте функцию, рисующую звезду с n вершинами.
import asyncio
import time
from turtle import Turtle

async def star(n, d, x):
    turtle = Turtle()
    q = 180 / n
    turtle.penup()
    turtle.setx(x)
    turtle.pendown()
    turtle.left(180)
    for _ in range(n):
        turtle.forward(d)
        turtle.left(180 - q)


async def main():
    await asyncio.gather(
        star(5, 150, -100),
        star(11, 150, 100)
    )

# Python 3.7+
asyncio.run(main())

time.sleep(2)

