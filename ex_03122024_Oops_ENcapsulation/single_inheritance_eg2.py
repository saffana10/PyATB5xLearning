class Parent:
    gold = "2kg"

    def BHK2(self):
        print("Parent's 2BHK")
        self.gold

class Child(Parent):

    def BHK3(self):
        print("Child's 3BHK")

parent = Parent()
child = Child()
child.BHK3()
print(child.gold)
