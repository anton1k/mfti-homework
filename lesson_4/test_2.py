import graphics as gr

window = gr.GraphWin("landscape", 1200, 800)

def rectangle(x1, y1, x2, y2, color, width=1):
    rectangle = gr.Rectangle(gr.Point(x1, y1), gr.Point(x2, y2))
    rectangle.setWidth(width)
    rectangle.setFill(color)
    rectangle.draw(window)

def circle(x, y, size, color):
    circle = gr.Circle(gr.Point(x, y), size)
    circle.setFill(color)
    circle.draw(window)

def polygon(x1, y1, x2, y2, x3, y3, color, width):
    polygon = gr.Polygon(gr.Point(x1, y1), gr.Point(x2, y2), gr.Point(x3, y3))
    polygon.setWidth(width)
    polygon.setFill(color)
    polygon.draw(window)

def line(x1, y1, x2, y2, width):
    line = gr.Line(gr.Point(x1, y1), gr.Point(x2, y2))
    line.setWidth(width)
    line.draw(window)


# фон
rectangle(1200, 400, 0, 0, 'blue')
rectangle(0, 400, 1200, 800, '#C0C0C0')
# облака
circle(100, 70, 25, '#ffffff')
circle(125, 70, 25, '#ffffff')
circle(140, 95, 25, '#ffffff')
circle(110, 95, 25, '#ffffff')
circle(80, 95, 25, '#ffffff')
# солнце
circle(900, 100, 70, 'yellow')
# дом
polygon(200, 300, 350, 150, 500, 300, 'brown', 7)
rectangle(200, 300, 500, 600, '#696969', 7)
rectangle(250, 350, 450, 500, 'yellow', 7)
line(250, 425, 450, 425, 7)
line(350, 350, 350, 500, 7)
# дерево
rectangle(900, 600, 925, 750, 'brown', 5)
polygon(825, 600, 910, 500, 1000, 600, 'green', 7)
polygon(825, 550, 910, 450, 1000, 550, 'green', 7)
polygon(825, 500, 910, 400, 1000, 500, 'green', 7)



window.getMouse()
window.close()