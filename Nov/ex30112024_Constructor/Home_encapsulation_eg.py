class Home:

    def __init__(self):
        self.pub_var = "father"
        self.__pri_var = "child"

    def mom(self):
        print(self.__pri_var)
        self.__wife()

    def __wife(self):
        print("Public variable ")

home = Home()
print(home.pub_var)
#print(home.__pri_var)
home.mom()
