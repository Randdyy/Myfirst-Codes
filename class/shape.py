import math
class Shape():
    ''' 前两个参数为矩形长宽，前三个参数为三角形三边，第四个参数为
    圆的半径，第五个为bool值，判断是否为圆
    '''
    __length = 0
    __width = 0
    __c = 0
    __r = 0
    def side(self,x ,y, z, r, Type = True):
        self.__length = x
        self.__width = y
        self.__z = z
        self.__r = r
        self.__Type = Type
    def get(self):
        self.length = self.__length
        self.width = self.__width
        self.r = self.__r
        self.z = self.__z
        self.Type = self.__Type

    def area(self):
        pass





class square(Shape):
    def area(self):
        if self.length == self.width and Type == True:
            return self.length^2


class triangle(Shape):
    def area1(self):
#        if self.length+self.width>self.c and self.c+self.length>self.width and self.c+self.width>self.length
        p = (self.length+self.width+self.__c)/2
        return sqrt(p*(p-self.length)*(p-self.width)*(p-self.c))



class circle(Shape):
    def area2(self):
        if Type == False:
            return pi*r^2


s = square(2,2,2,2)
print(s.area)


