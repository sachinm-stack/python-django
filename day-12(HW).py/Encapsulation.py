class BankAccount:

    def __init__(self, owner, balance, pin):
        self.owner     = owner
        self.__balance = balance   # private
        self.__pin     = pin       # private

    def get_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        return "Incorrect PIN"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.__balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            raise ValueError("Incorrect PIN!")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if amount > self.__balance:
            raise ValueError("Insufficient balance!")
        
        self.__balance -= amount
        print(f"Withdrawn ₹{amount}")


# Test
acc = BankAccount('Rahul', 10000, '1234')

print(acc.get_balance('1234'))    # 10000
print(acc.get_balance('0000'))    # Incorrect PIN

acc.deposit(5000)                 # Deposited ₹5000
acc.withdraw(3000, '1234')        # Withdrawn ₹3000

# print(acc.__balance)  ❌ AttributeError