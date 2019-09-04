import graphics as gr

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(400, 700)
velocity = gr.Point(2, 0)
acceleration = gr.Point(0, 0)

rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
rectangle.setFill('green')
rectangle.draw(window)

sun = gr.Circle(gr.Point(400, 400), 50)
sun.setFill('yellow')
sun.draw(window)

circle = gr.Circle(coords, 10)
circle.setFill('red')
circle.draw(window)

def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point


def update_coords(coords, velocity):
    return add(coords, velocity)


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)

    G = 2000

    return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)

def add2(point_1, point_2):
    new_point = gr.Point(point_2.x - point_1.x, point_2.y - point_1.y)
    return new_point 

while True:
    acceleration = update_acceleration(coords, gr.Point(400, 400))
    
    coords2 = update_coords(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    movecoords = add2(coords, coords2)
    x = movecoords.getX()
    y = movecoords.getY()
    circle.move(x, y)
    
    coords = coords2

    gr.time.sleep(0.02)

