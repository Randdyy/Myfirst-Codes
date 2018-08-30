class Person():

    def __init__(self,f,l):
        self.l = l
        self.f = f
#    @property
    def full_Name(self):
        return '{} {}'.format(self.f, self.l)


#    def getName(self):
#        return self.full_Name

    def setName(self,newName):
        self.newName1 = newName.split(' ')[0]
        self.newName2 = newName.split(' ')[1]
        self.f = self.newName1
        self.l = self.newName2
        self.__init__( self.f, self.l)


    full_Name = property(full_Name, setName)


zhangsan = Person('zhang','san')
print(zhangsan.full_Name)
zhangsan.full_Name  = 'li si'
print(zhangsan.full_Name)

