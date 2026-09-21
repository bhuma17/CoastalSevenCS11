
from abc import ABC, abstractmethod


class BankAccount(ABC):

    bank_name = "ABC Bank"

    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative")

    def deposit(self, amount):

        if amount > 0:
            self.balance = self.balance + amount
            print("Deposited:", amount)
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be positive")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)

    @abstractmethod
    def calculate_interest(self):
        pass

    def __str__(self):
        return (
            f"Account Number: {self.account_number}\n"
            f"Account Holder: {self.account_holder}\n"
            f"Balance: {self.balance}"
        )


class SavingsAccount(BankAccount):

    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):

        interest = self.balance * self.interest_rate / 100

        return interest


class CurrentAccount(BankAccount):

    def calculate_interest(self):

        return 0


savings = SavingsAccount(
    101,
    "Srujana",
    10000,
    5
)

current = CurrentAccount(
    102,
    "Chaitanya",
    20000
)


print("----- SAVINGS ACCOUNT -----")

print(savings)

savings.deposit(5000)
print("Savings account balance after the deposit:", savings.balance)

savings.withdraw(2000)

print("Current Balance:", savings.balance)

print("Interest:", savings.calculate_interest())


print("\n----- CURRENT ACCOUNT -----")

print(current)

current.deposit(5000)
print("Current account balance after the deposit:",current.balance)

current.withdraw(3000)

print("Current Balance:", current.balance)

print("Interest:", current.calculate_interest())