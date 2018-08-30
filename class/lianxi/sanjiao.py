import math
class SanJiao():

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def judge(self,x, y, z):
        if x + y > z and x + z > y and y + z > x:
            print("这三条边能够成三角形")
        else:
            raise TypeError('三角形你懂不')

    def area(self):
        a = (self.__x + self.__y + self.__z)/2
        return math.sqrt(a*(a-self.__x)*(a-self.__y)*(a-self.__z))
tri = SanJiao(10,11,12)
print(tri.area())
