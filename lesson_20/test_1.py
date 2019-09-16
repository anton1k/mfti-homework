class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    def __rmul__(self, other):
        return Vector(other.x * self.x, other.y * self.y)
    def __neg__(self, other):
        return Vector(-other.x -self.x, -other.y -self.y)

    def __str__(self):
        return  'x = {}, y = {}'.format(self.x, self.y)
