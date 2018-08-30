

class Screen:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def get(self):
        return self.width,self.height


    def sett(self,new):
        self.new_width = new.split(' ')[0]
        self.new_height = new.split(' ')[1]
        self.__init__(self.new_width,self.new_height)

    def getApi(self):
        return (self.width,'*',self.height)


    get = property(get, sett)


aaa = Screen(20,30)
print(aaa.get)
aaa.get = '50 80'
print(aaa.get)
print(aaa.getApi())

