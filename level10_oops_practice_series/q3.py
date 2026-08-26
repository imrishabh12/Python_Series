# Q3. Create a BankAccount class with deposit and withdrawal methods.

class BankAccount:

    def display_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


account = BankAccount()

account.balance = 1000

account.display_balance()

account.deposit(500)
account.display_balance()

account.withdraw(300)
account.display_balance()