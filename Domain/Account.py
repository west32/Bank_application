class Account:
    def __init__(self, account_id, name, balance: float, open_transaction=None):
        self.account_id = account_id
        self.name = name
        self.open_transaction = open_transaction
        self.balance = balance

    def __str__(self):
        return f"[ {self.account_id}, name:{self.name}, balance:{self.balance} pln] "

    def add_money(self, money_amount):
        self.balance += money_amount
        return self.balance

    def sub_money(self, money_amount):
        self.balance -= money_amount
        return self.balance

    def block_account(self, transaction: str):
        if self.open_transaction is not None:
            raise Exception("Account has been blocked")
        # self.open_transaction = transaction.uuid
        self.open_transaction = transaction

    def unlock_account(self, transaction: str):
        # if self.open_transaction == transaction.uuid:
        #     self.open_transaction = None
        if self.open_transaction == transaction:
            self.open_transaction = None
