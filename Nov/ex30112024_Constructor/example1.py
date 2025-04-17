class Car:

    def __init__(self,o_name , o_model ,o_year):
        self.name = o_name
        self.model = o_model
        self.year =  o_year

    def car_info(self):
        print("Car name is" , self.name)
        print("Car model is" , self.model)
        print("Car year is" , self.year)

lamborghini = Car("lambo","V6","2024")
lamborghini.car_info()
print("------")
mg_hector = Car("Hector","1.5+Turbo","2025")
mg_hector.car_info()



