# Нарисуйте смайлик с помощью написанных функций рисования круга и дуги
import turtle

def gotos(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def circle_min():
    turtle.begin_fill()
    turtle.color ('black', 'blue')
    turtle.circle(15, 360)
    turtle.end_fill()


turtle.shape('turtle')

turtle.right(-90) 

turtle.begin_fill()
turtle.color ('black', 'yellow')
turtle.circle(100, 360)
turtle.end_fill()

gotos(-130, 40)
circle_min()

gotos(-40, 40)
circle_min()

gotos(-100, 10)
turtle.pensize(10)
turtle.backward(25)

gotos(-50, -30)
turtle.right(180)
turtle.pencolor('red')
turtle.circle(-50, 180)
turtle.hideturtle()

turtle.mainloop()

