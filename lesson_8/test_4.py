# Три копии кривой Коха, построенные (остриями наружу) на сторонах правильного треугольника, образуют замкнутую кривую бесконечной длины, называемую снежинкой Коха. Нарисуйте ee.
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
    l //= 3
    draw(l, n-1)
    turtle.left(60)
    draw(l, n-1)
    turtle.right(120)
    draw(l, n-1)
    turtle.left(60)
    draw(l, n-1)
   
for _ in range(3):  
    draw(400, 3)
    turtle.right(120)
    

time.sleep(2)