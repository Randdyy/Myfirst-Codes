import random
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getLength(self):
        pass



class Line(Point):

    def getLength(self):
        self.length = math.sqrt(self.x**2+self.y**2)
        return self.length



L = Line(3,4)
print(L.getLength())
