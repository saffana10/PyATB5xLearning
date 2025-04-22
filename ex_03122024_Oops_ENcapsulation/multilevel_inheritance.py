class Grandfather:
    gold = "1kg"

    def BHK1(self):
        print("1BHK")

class Father(Grandfather):
    diamond = "22 karat"

    def BHK2(self):
        print("2BHK")

class Son(Father):
    btc = "1BTC"

    def BHK3(self):
        print("3BHK")

son = Son()
son.BHK2()
print(son.diamond)

father = Father()
print(father.gold)
