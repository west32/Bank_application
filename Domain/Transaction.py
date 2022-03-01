from datetime import datetime
import uuid

from Domain.Account import Account
from Domain.Transaction_Status import Status


class Transaction:
    def __init__(self, a_account: Account, b_account: Account, money_amount: float):
        self.a_account = a_account
        self.b_account = b_account
        self.money_amount = money_amount
        self.date = datetime.now()
        self.uuid = uuid.uuid4()
        self.status = Status.OPEN

    def __str__(self):
        return f" from account {self.a_account} to account {self.b_account} transfer {self.money_amount}, date: {self.date}, transaction id: {self.uuid}, Status: {self.status}"

    def block_accounts(self):
        self.a_account.block_account(self.uuid)
        self.b_account.block_account(self.uuid)

    def unlock_accounts(self):
        self.b_account.unlock_account(self)
        self.a_account.unlock_account(self)

    def check_balances(self):
        if self.a_account.balance < self.money_amount:
            self.unlock_accounts()
            self.status = Status.REJECTED
            raise Exception(
                f"Not enough money to transfer! Your current account balnce: {self.a_account.balance},{self.status}")

    def transfer(self):
        self.block_accounts()
        self.check_balances()
        self.a_account.sub_money(self.money_amount)
        self.b_account.add_money(self.money_amount)
        self.unlock_accounts()
        self.status = Status.REALISED
