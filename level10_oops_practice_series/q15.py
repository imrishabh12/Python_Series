# Q15. Build a small Bank Management System using classes.


class BankAccount:

    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")

    def display(self):
        print("\nAccount Number:", self.account_number)
        print("Name:", self.name)
        print("Balance:", self.balance)


account = BankAccount(
    1001,
    "Rishabh",
    5000
)

while True:

    print("\n--- Bank Management System ---")
    print("1. Display Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        account.display()

    elif choice == "2":

        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "3":

        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "4":

        print("Thank you for using the Bank Management System.")
        break

    else:

        print("Invalid choice.")