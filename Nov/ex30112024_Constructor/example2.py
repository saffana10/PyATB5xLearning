 # web automation
from dotenv import load_dotenv
class Login:

    def __init__(self,email_arg,pass_arg):
        self.email = email_arg
        self.password = pass_arg

    def login_success(self):
        if self.email == "saffana@gmail.com" and self.password == "Saffana@123":
            print("Login success")
        else:
            print("Login failed , check your email and password")

# email = input("Enter your email id\n")
# password = input("Enter your password\n")

load_dotenv()
import os
email = os.getenv("Email")
password = os.getenv("Password")

#login = Login("saffana@123","pass")
login = Login(email,password)
login.login_success()