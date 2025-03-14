class BankAccount:
     def __init__(self, account_number, balance=0):
       self.account_number = account_number
       self.balance = balance
     def deposit(self, amount):
       self.balance += amount
       print(f"Deposited {amount}. New balance: {self.balance}")
     def withdraw(self, amount):
       if amount <= self.balance:
          self.balance -= amount
          print(f"Withdrew {amount}. New balance: {self.balance}")
       else:
            print("Insufficient balance")
 account = BankAccount("12345")
 account.deposit(1000)
 account.withdraw(500)
