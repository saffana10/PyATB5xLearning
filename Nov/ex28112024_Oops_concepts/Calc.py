class Calc:

    def __init__(self):
        print("DC")

    def sum(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b

obj_ref = Calc()
a = float(input("Enter the value of a:\n"))
b = float(input("ENter the value of b:\n"))

sum1 = obj_ref.sum(a,b)
sub1 = obj_ref.sub(a,b)
mul1 = obj_ref.mul(a,b)
div1 = obj_ref.div(a,b)
print(sum1,sub1,mul1,div1)