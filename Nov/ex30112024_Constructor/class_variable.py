

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
       return self.name
       return self.age

    def talk(self):
        return self.name

amit = Person("Amit" ,"25")
print(amit.name)
print(amit.age)
pramod = Person("Pramod" , "30")
print(pramod.age)
print(pramod.name)

print("who is walking", amit.walk())
print("who is talking" ,amit.talk())
print("who is walking" , pramod.walk())
print("who is talking" ,pramod.talk())