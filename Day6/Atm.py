class InsufficientBalanceError(Exception):
    pass


class Atm:

    def __init__(self,Acc_holder,balance):
        self.Acc_holder = Acc_holder
        self.__balance = balance

    def deposit(self,amount):
        self.amount = amount
        self.__balance +=self.amount
        print(f"Deposited Amount:{self.amount}  New Balance:{self.__balance}")

    def withdraw(self,amount):
        self.amount = amount
        if amount > self.__balance:
            raise InsufficientBalanceError("No balance in your account")
        self.__balance-=self.amount
        print(f"Withdraw Amount:{self.amount}  New Balance:{self.__balance}")

    def check_balance(self):
        print(f"Your Current balance :{self.__balance}")


Account1 = Atm("Rajesh",5000)

try:
    Account1.deposit(int(input("Enter deposit amount:")))
    Account1.withdraw(int(input("Enter withdraw amount:")))
    Account1.check_balance()

except InsufficientBalanceError as e:
    print(e)


        
