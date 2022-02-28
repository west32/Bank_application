import uuid

from Account import Account
from Money_Transfer_Command import MoneyTransferCommand
from Transaction import Transaction
import datetime


# import Money_Transfer_Command

class MoneyTransferUseCase:
    def __init__(self, accounts_data_base):
        self.accounts_data_base = accounts_data_base

    def unlock_accounts(self,a_account, b_account, transaction_log):
        a_account.unlock_account(transaction_log)
        b_account.unlock_account(transaction_log)

    def block_accounts(self, a_account, b_account, transaction_log):
        a_account.block_account(transaction_log)
        b_account.block_account(transaction_log)

    # def update_accounts_balances(self, a_account:Account, b_account, command_transfer:MoneyTransferCommand):
    #     a_account.sub_money(command_transfer.money_amount)
    #     b_account.add_money(command_transfer.money_amount)

    def transfer(self, command_transfer: MoneyTransferCommand):
        if command_transfer.a_account_number not in self.accounts_data_base or command_transfer.b_account_number not in self.accounts_data_base:
            raise Exception("number account has not found")

        a_account = self.accounts_data_base[command_transfer.a_account_number]
        b_account = self.accounts_data_base[command_transfer.b_account_number]
        transaction_log = Transaction(a_account.account_id, b_account.account_id, command_transfer.money_amount,
                                      datetime.datetime.now(), uuid.uuid4(), "OPEN")
        # TODO wykorzystac typ enum do statusu
        self.block_accounts(a_account, b_account, transaction_log)

        if self.accounts_data_base[command_transfer.a_account_number].balance < command_transfer.money_amount:
            self.unlock_accounts(a_account, b_account, transaction_log)
            raise Exception(
                f"Not enough money to transfer! Your current account balnce: {self.accounts_data_base[command_transfer.a_account_number].balance}")
        # self.update_accounts_balances(a_account, b_account, command_transfer)
        self.accounts_data_base[command_transfer.a_account_number].sub_money(command_transfer.money_amount)
        self.accounts_data_base[command_transfer.b_account_number].add_money(command_transfer.money_amount)
        self.unlock_accounts(a_account, b_account, transaction_log)

   # TODO dont repeat yourself wyekstrahowac czesci wspolne, powyciagac z transferu wspolcze czesci na inne funkcje
        # 1/2 rozdzial uncle bob,

