class Bank:

    def __init__(self,account_number,balance):
        self.__account_number = account_number # private variable cannot be accessed directly it can be accessed through a function only
        self.balance = balance

    def check_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount

    def show_me_account_number(self,is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not allowed")

    def __internal_private_method(self):
        print("Private method, can be access by only class")

    def access_to_private_method(self):
        self.__internal_private_method();

bank = Bank("9876543210",500)

bank.check_balance()
#print(bank.balance)  # can be called directly as balance is public variable
bank.deposit(500)
bank.check_balance()
print("---")

bank.show_me_account_number(False)
#bank.__internal_private_method()
bank.access_to_private_method()
#bank.__account_number()

