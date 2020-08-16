class InsufficientAmount(Exception):
    pass


class Wallet:
    def __init__(self, balance=0):
        self.balance = balance

    def spend_cash(self, amount):
        if amount > self.balance:
            raise InsufficientAmount("You can not spend more than your current balance")

        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount
