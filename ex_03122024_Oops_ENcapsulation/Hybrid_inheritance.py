class A:

    def methodA(self):
        print("A")

class B(A):

    def methodB(self):
        print("B")

class C(A):

    def methodC(self):
        print("C")

class D(B,C):

    def methodD(self):
        print("D")

d = D()
d.methodD()
d.methodC()
d.methodB()
d.methodA()

