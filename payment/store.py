from payment.transaction import Transaction

class Store:

    def __init__(self):
        self.__balance = 0
        self.__history = []

    def add_cash(self, payment_method, amount):

        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        if payment_method.process_payment(amount):
            self.__balance += amount
            transaction = Transaction("CREDIT", amount, self.__balance)
            self.__history.append(transaction)
            print("Amount added successfully!")

    def refund(self, amount):

        if amount <= 0:
            raise ValueError("Refund amount must be greater than 0")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount
        transaction = Transaction("REFUND", amount, self.__balance)
        self.__history.append(transaction)
        print("Refund processed successfully!")

    def show_balance(self):
        print(f"Current Balance: ₹{self.__balance}")

    def show_history(self):

        if not self.__history:
            print("No transactions found.")
            return

        print("\n------ Transaction History ------")
        for txn in self.__history:
            print(txn)
        print("---------------------------------")
