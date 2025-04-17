#Encapsulation - Hide data members (instance variables)

class Login:

    def __init__(self):
        self.password = "saffana" # public instance variable
        self.__password = "abc"  #private instance variable

    def change_password(self):
        print(self.password)
        print(self.__password)
 #private variable is available only in the class and methods
 #public is available to all
login = Login()
#login.change_password()
print(login.password)
print(login.change_password())
print(login.__password)