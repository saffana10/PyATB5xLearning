#Method overloading is not supportedin python
class Calc:

    def sum(self,a,b):
        return a+b

    def sum(self,a,b,c):
        return a+b+c

calc = Calc()
calc.sum(3,4)