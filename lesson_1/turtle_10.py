# Нарисуйте «бабочку» из окружностей. Используйте функцию, рисующую окружность.
import time

import turtle
import math as m

b = 1
loops = 20    
n = 200                 
r = 20    
i = 0              
                        
turtle.shape('turtle')
turtle.left(90)
def more_agles(n):
    q=360/n
    L = 2 * r * m.sin(m.pi / n)
    while n>0:
        turtle.forward(L)
        if b > 0:
            turtle.left(q)
        else:
            turtle.right(q)
        n -= 1
       
while i < loops:
    more_agles(n)
    if i%2 == 1:
        r += 5
    b *= -1
    i += 1
                         
    


time.sleep(1)