class Area():
    __length = 0
    __width = 0

#    def __init__(self, l, w):
#        self.__length = l
#        self.__width = w

    def getwide(self):
        return self.__width

    def getlong(self):
        return self.__length


    def setlong(self, l):
        self.__length = l
        return self.__length
    def setwide(self, w):
        self.__width = w

    def area(self):
        areaa = self.__length*self.__width
        return areaa

    def judge(self):
        if not self.__width == self.__length:
            print("这是一个chang方形")




class square(Area):

    def area(self):
        return self.__length^2




S = square()
S.setlong(50)
S.area()



#rectangle = Area()
#rectangle.setlong(10)
#rectangle.setwide(20)
#print(rectangle.area())
#rectangle.judge()

