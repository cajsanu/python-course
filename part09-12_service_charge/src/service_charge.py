# WRITE YOUR SOLUTION HERE:


class BankAccount: 
    def __init__(self, name: str, account_number: str, balance: float):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance
        
    def __service_charge(self, balance):
        self.__balance -= self.__balance*0.01
    
    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge(self.__balance)
        
    def withdraw(self, amount: float):
        if amount <= self.__balance:
            self.__balance -= amount
        else: 
            pass
        self.__service_charge(self.__balance)
        
    @property
    def balance(self):
        return self.__balance
        
        
# account = BankAccount("Randy Riches", "12345-6789", 1000)
# account.withdraw(100)
# print(account.balance)
# account.deposit(100)
# print(account.balance)
        
        

