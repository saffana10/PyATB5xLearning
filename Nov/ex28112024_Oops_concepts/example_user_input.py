class Person:

    def __init__(self):
        self.name = input("Enter the name of a person\n")
        self.age = input("Enter the age\n")
        self.phone = input("Enter the phone number\n")
        self.occupation = input("Enter your occupation\n")

    def function_to_display(self):
        print(f"Name of a person is:" +self.name , f"Age of a person is:" + self.age ,f"phone number of a person is:" + self.phone)


Person1= Person()
Person1.function_to_display()
