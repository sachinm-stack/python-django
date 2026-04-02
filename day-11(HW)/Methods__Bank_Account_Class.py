class BankAccount:

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
            return
        self.balance -= amount
        print(f"Withdrawn {amount}. Balance: {self.balance}")

    def show_balance(self):
        print(f"Balance: {self.balance}")


# Test it:
acc1 = BankAccount('Rahul', 'ACC001', 1000)

acc1.show_balance()       # Balance: 1000
acc1.deposit(500)         # Deposited 500. Balance: 1500
acc1.withdraw(200)        # Withdrawn 200. Balance: 1300
acc1.withdraw(2000)       # Insufficient balance!