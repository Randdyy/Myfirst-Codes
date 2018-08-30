class A():
    def __init__(self):
        print('in A')
        print('out A')


class B(A):
    def __init__(self):
        print('in B')
        super(B,self).__init__()
        print('out B')

class C(A):
    def __init__(self):
        print('in C')
        super(C,self).__init__()
        print('out C')



class D(B, C):
    def __init__(self):
        print('in D')
        super(D,self).__init__()
        print('out D')



d = D()

