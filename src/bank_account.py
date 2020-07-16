class BankAccount:

    def __init__(self, name):
        self.name = name
        self.balance = 0.00
        self.transaction_fee = 0.00

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount, transaction_fee=0.00):
        if transaction_fee < 0:
            self.transaction_fee = 0.00

        if transaction_fee > 0:  # not negative
            self.transaction_fee = transaction_fee

        amt_to_withdraw = amount + self.transaction_fee
        if amt_to_withdraw < 0:
            return
        if amt_to_withdraw > self.balance:
            return
        self.balance = self.balance - amt_to_withdraw


ba = BankAccount("abc")

ba.deposit(40)
print("balance=", ba.balance)

ba.withdraw(10)
print("balance=", ba.balance)

ba.withdraw(10,0.5)
print("balance=", ba.balance)

ba.withdraw(10,1.5)
print("balance=", ba.balance)

ba.withdraw(4,-1.5)
print("balance=", ba.balance)