# Нарисуйте кривую Коха. Процесс её построения выглядит следующим образом: берём единичный отрезок, разделяем на три равные части и заменяем средний интервал равносторонним треугольником без этого сегмента. В результате образуется ломаная, состоящая из четырёх звеньев длины 1/3. На следующем шаге повторяем операцию для каждого из четырёх получившихся звеньев и т. д… Предельная кривая и есть кривая Коха.

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
   
  
draw(400, 4)