class Listinfo:
    def __init__(self, l=[]):
        self.l = l


    def Add(self,element):
        if isinstance(element, int) or isinstance(element,str):
            self.l.append(element)
            return self.l
        else:
            raise TypeError

    def Combine(self,l1=[],l2=[]):
        l3 = []
        if len(l1)>=len(l2):
            for i in range(0,len(l2)):
                if isinstance(l1[i], str) and isinstance(l2[i],str):
                    l3.append(l1[i]+l2[i])
                elif isinstance(l1[i], int) and isinstance(l2[i],int):
                    l3.append(l1[i]+l2[i])
                else:
                    raise TypeError
            return l3

        else :
            for i in range(0,len(l1)):
                if isinstance(l1[i], str) and isinstance(l2[i],str):
                    l3.append(l1[i]+l2[i])
                elif isinstance(l1[i], int) and isinstance(l2[i],int):
                    l3.append(l1[i]+l2[i])
                else:
                    raise TypeError
            return l3

    def delt(self):
        fin = self.l[len(self.l)-1]
        del self.l[len(self.l)-1]
        return fin


lis1=[123,213,'bbb','asdasda']
lis2=[321,666,'aaa']
L = Listinfo(lis1)
print(L.Add('charu'))

print(L.Combine(lis1,lis2))




