class A:
    def funcA(self):
        print("A")

class B(A):
    def funcB(self):
        print("B")

class C(A):
    def funcC(self):
        print("C")

class D(B, C):
    def funcD(self):
        print("D")

d = D()
d.funcA()
d.funcB()
d.funcC()
d.funcD()
d = D()
d.funcA()
d.funcB()
d.funcC()
d.funcD()
