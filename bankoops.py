# Define the BankAccount class
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance 
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive!")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:  
            self.__balance -= amount
            print(f"Withdrawn: ${amount}")
        elif amount > self.__balance:
            print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive!")
    def check_balance(self):
        print(f"Current Balance: ${self.__balance}")
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
account.check_balance()
account.withdraw(1500)
account.deposit(-200)
