class Father():
    height = 180
    weight = 150
    __name = 'father'
    def say(self):
        print("我{}斤，我的身高是{}，我的名字是{}".format(self.weight,self.height,self.__name))
        self.__cost()
    def __cost(self):
        print("我会花钱")


class Son(Father):

    height = 190
    __name = 'son'
    def speak(self):
        print("height {}  weight{}name{}".format(self.height,self.weight,self.__name))


SSS=Son()
SSS.say()
SSS.speak()
