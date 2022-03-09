from Domain.Transaction import Transaction
from Service.Money_Transfer_Command import MoneyTransferCommand, MoneyTransferCommandException
from Repository.Account_Repository import AccountRepository


class MoneyTransferUseCase:
    def __init__(self):
        self.accounts_data_base = AccountRepository()

    def transfer(self, command_transfer: MoneyTransferCommand):
        a_account = self.accounts_data_base.find_by_account_number(command_transfer.a_account_number)
        b_account = self.accounts_data_base.find_by_account_number(command_transfer.b_account_number)
        if a_account is None or b_account is None:
            raise TransferUseCaseException("number account has not found")
        transaction = Transaction(
            a_account,
            b_account,
            command_transfer.money_amount)
        transaction.transfer()
        print(transaction)


class TransferUseCaseException(MoneyTransferCommandException):
    def __init__(self, message):
        self.message = message
