class Father:

    def father_money(self):
        return 5

    def home(self):
        print("Father's home")

class Mother:

    def mother_money(self):
        return 2

    def home(self):
        print("Mother's home")

#class Son(Father, Mother):
class Son(Mother, Father):  # First come first serve

    def info(self):
        print("Son")



son = Son()
print(son.mother_money())
print(son.father_money())
son.info()
son.home()
