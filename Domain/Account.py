class Account:
    def __init__(self, account_number, name, balance: float, open_transaction=None, id =None):
        self.account_number = account_number
        self.name = name
        self.open_transaction = open_transaction
        self.balance = balance
        self.id = id

    def __str__(self):
        return f"[ account_number: {self.account_number}, name:{self.name}, balance:{self.balance} pln] "

    def serialize(self):
        return {
            'name': self.name,
            'account_number': self.account_number,
            'account_balance': self.balance,
            'id': str(self.id)
        }

    def add_money(self, money_amount):
        self.balance += money_amount
        return self.balance

    def sub_money(self, money_amount):
        self.balance -= money_amount
        return self.balance

    def block_account(self, transaction: str):
        if self.open_transaction is not None:
            raise Exception("Account has been blocked")
        self.open_transaction = transaction

    def unlock_account(self, transaction: str):
        if self.open_transaction == transaction:
            self.open_transaction = None
