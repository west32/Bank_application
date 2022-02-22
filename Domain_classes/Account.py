class Account:
    def __init__(self, account_id, name, balance: int, open_transaction=None):
        self.account_id = account_id
        self.name = name
        self.open_transaction = open_transaction
        self.balance = balance

    def __str__(self):
        return f" account number:{self.account_id}, name:{self.name}, balance:{self.balance} pln"

    def add_money(self):
        pass

    def sub_money(self):
        pass

    def block_account(self, transfer_id):
        # if open_transaction not null throw exeption
        pass

    def unlock_account(self, tranfer_id):
        pass
