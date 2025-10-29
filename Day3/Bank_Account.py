class BankAccount():

    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance


    def deposit(self,amount):
        self.__balance += amount
        print(self.__balance)


    def withdraw(self,amount):
        self.__balance -= amount
        print(self.__balance)


Account1 = BankAccount("Rajesh" , 5000)

Account1.deposit(500)
Account1.withdraw(1000)
