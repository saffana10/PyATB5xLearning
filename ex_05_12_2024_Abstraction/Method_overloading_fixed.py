# class Calc:
#
#     def sum(self,a,b):
#         return a+b
#
#     def sum(self,a,b,c=2):
#         return a+b+c
#
# calc = Calc()
# result = calc.sum(3,4)
# print(result)

# two functions cannot have the same name in python

class Calc:

    def sum(self,*args):
        for a in args:
            print(a)

calc = Calc()
calc.sum(1)
print("----")
calc.sum(3,4)
print("---")
calc.sum(4,5,6)
