from calendar import month


class Dog:
# Attributes
    name = "Rancho"
    breed = None
    weight = None

#constructor is automatically called when an object is created
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

# Behaviour
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Who is sleeping ->" + self.name)

    def talk(self):
        pass


chow_ref = Dog("rancho","mastiff")
mow_ref = Dog("Tommy","husky")

print(chow_ref.name)
print(chow_ref.breed)
chow_ref.sleep()
print(id(chow_ref))

print(mow_ref.name)
print(mow_ref.breed)
mow_ref.sleep()
print(id(mow_ref))

