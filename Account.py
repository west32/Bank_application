from Money_Transfer_Command import MoneyTransferCommand
from Money_Transfer_Usecase import MoneyTransferUseCase
from Transaction import Transaction


class Account:
    def __init__(self, account_id, name, balance: float, open_transaction=None):
        self.account_id = account_id
        self.name = name
        self.open_transaction = open_transaction
        self.balance = balance

    def __str__(self):
        return f" account number:{self.account_id}, name:{self.name}, balance:{self.balance} pln"

    def add_money(self, money_amount):
        self.balance += money_amount
        return self.balance

    def sub_money(self, money_amount):
        self.balance -= money_amount
        return self.balance

    def block_account(self, transaction: Transaction):
        if self.open_transaction is not None:
            raise Exception("Account has been blocked")
        self.open_transaction = transaction.uuid


    def unlock_account(self, transaction: Transaction):
        if self.open_transaction == transaction.uuid:
            self.open_transaction = None
