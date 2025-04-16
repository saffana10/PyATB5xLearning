class Dog:
# Attributes
    name = "Rancho"
    breed = None
    weight = None

#constructor is automatically called when an object is created
    def __init__(self):
        print("I will be called automatically")
# Behaviour
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleeping")

    def talk(self):
            pass


chow_ref = Dog()
mow_ref = Dog()

#name called is same that's why the output will be the same
print(chow_ref.name)
print(mow_ref.name)