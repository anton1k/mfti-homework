# Нарисуйте Канторово множество. Канторово множество нулевого порядка - горизонтальный отрезок. Удалив среднюю треть получим множество первого порядка. Повторяя данную процедуру получим остальные множества.

import turtle

turtle.shape('turtle')

def cantor_set(x, y, l, n):
    if n == 0:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        turtle.forward(l)
        return

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.forward(l)

    cantor_set(x, y-30, l/3, n-1)
    cantor_set(x + l*2/3, y-30, l/3, n-1)

L = 600
N = 3
X = -L/2
Y = 15 * N


turtle.penup()
turtle.goto(X, Y)
turtle.pendown()

cantor_set(X, Y, L, N)

turtle.exitonclick() # click to exit