class MyList():
    __mylist = []


    def __init__(self, *args):
        for i in args:
            self.__mylist.append(i)

    def __sub__(self, x):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] - x
        return self.__mylist

    def __add__(self, x):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] + x
        return self.__mylist

    def __mul__(self, x):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] * x
        return self.__mylist
    def __truediv__(self, x):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] / x
        return self.__mylist



A = MyList(2,2,2,4,6)
print(A / 2)

