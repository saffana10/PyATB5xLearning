#Method Overloading
class  Dog:

    def bark(self):
        print("Dog is barking")

    def bark(self,breed):
        print(f"Dog with {breed} is barking")

dog = Dog()
dog.bark("chow")
