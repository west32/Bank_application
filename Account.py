from Money_Transfer_Command import MoneyTransferCommand
from Money_Transfer_Usecase import MoneyTransferUseCase


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

    def block_account(self):
        if self.open_transaction is not None:
            raise Exception(f"Acconunt {self.account_id} has been blocked")


    def unlock_account(self, tranfer_id):
        pass
