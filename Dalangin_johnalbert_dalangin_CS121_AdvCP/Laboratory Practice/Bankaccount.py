from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self, account_number, balance = 0):
        self._account_number = account_number
        self._balance = balance
    
    @property
    def account_number(self):
        return self._account_number
        
    @property
    def balance(self):
        return self._balance
        
    @abstractmethod
    def withdraw(self, amount):
        pass
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def display_account_type(self):
        pass
    
    
    
class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self._balance += amount
        
    def withdraw(self, amount):
        if self._balance - amount >= -5000:
            self._balance -= amount
        
    def display_account_type(self):
        return "Current Account"

class SavingsAccount(BankAccount):
    
    def deposit(self, amount):
        self._balance += amount
        
    def withdraw(self, amount):
        if self._balance - amount >= -5000:
            self._balance -= amount
            
    def display_account_type(self):
        return "Savings Account"


def print_account_details(account):
    print(f"Account Number: ",{account.account_number})
    print(f"Balance: ",{account.balance})
    print(f"Type: ",{account.display_account_type()})
    print("----------------------------------")
    
if __name__ == "__main__":
    acc1 = CurrentAccount("SA123", 1200)
    acc2 = SavingsAccount("CA456", -200)
    
    acc1.deposit(200)
    acc2.withdraw(4800)
    
print_account_details(acc1)
print_account_details(acc2)
