from datetime import datetime

class Transaction:

    def __init__(self, transaction_type, amount, balance):
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp} | {self.transaction_type} | ₹{self.amount} | Balance: ₹{self.balance}"
