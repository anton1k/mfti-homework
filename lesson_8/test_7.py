# Нарисуйте кривую дракона. Кривая дракона нулевого порядка - горизонтальный отрезок. 

'''пример из интернета'''
import turtle

turtle.shape('turtle')
turtle.speed('fastest')

def dragon(size, level, direction=45):
    size /= 1.41421
    if level:
        turtle.right(direction)
        dragon(size, level-1, 45)
        turtle.left(direction * 2)
        dragon(size, level-1, -45)
        turtle.right(direction)
    else:
        turtle.forward(size)
 

dragon(200, 7)

turtle.exitonclick() # click to exit