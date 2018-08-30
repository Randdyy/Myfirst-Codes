class Ticket():

    '''
    Ticket(num1,num2,bool)第一个参数是社会青年人数，第二个值是学生数，第三个值是判断是否为节假日
    '''

    price =100


    def __init__(self, x, y, Holiday = False):
        self.num_man = x
        self.num_stu = y
        self.Holiday = Holiday
        self.isHoliday()

    def cost(self):
        self.total = self.num_man*self.price + self.num_stu*self.price/2
#        print(self.total)
        return self.total

    def isHoliday(self):
        if self.Holiday :
            self.price = 120.0



T = Ticket(2, 1,True)
F = T.cost()
print(F)
T2 = Ticket(2, 1,False)
F2 = T2.cost()
print(F2)
F3 = F - F2
print("节假日比非节假日省{}".format(F3))





