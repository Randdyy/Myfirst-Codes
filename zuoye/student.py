class Student:
    def __init__(self,name, age, mark =[]):
        self.name = name
        self.age = age
        self.mark = mark

    def getName(self):
        return self.name


    def getAge(self):
        return self.age

    def getMaxMark(self):
        return max(self.mark)



A = Student('a',12,[222,233,444])

print(A.getMaxMark())
