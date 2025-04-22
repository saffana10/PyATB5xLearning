class Father:
    key = "2BHK"

    def car(self):
        print("Father has a alto")
        self.key


class Son(Father):
    key2 = "3BHK"

    def xuv(self):
        print("Mg Hector")
        self.key2

father = Father()
father.car()
print(father.key)

son = Son()   #single inheritance
son.xuv()
print(son.key2)
son.car()