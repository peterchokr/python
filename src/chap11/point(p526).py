class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y 

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1+p2)