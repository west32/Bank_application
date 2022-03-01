from Domain.Transaction import Transaction

# import Money_Transfer_Command
from Service.Money_Transfer_Command import MoneyTransferCommand


class MoneyTransferUseCase:
    def __init__(self, accounts_data_base):
        self.accounts_data_base = accounts_data_base

    def transfer(self, command_transfer: MoneyTransferCommand):
        if command_transfer.a_account_number not in self.accounts_data_base or command_transfer.b_account_number not in self.accounts_data_base:
            raise Exception("number account has not found")
        transaction = Transaction(
            self.accounts_data_base[command_transfer.a_account_number],
            self.accounts_data_base[command_transfer.b_account_number],
            command_transfer.money_amount)
        transaction.transfer()
        print(transaction)
