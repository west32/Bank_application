from Domain.Transaction import Transaction
from Repository.Memory_Transaction_Repository import MemoryTransactionRepository
from Service.Money_Transfer_Command import MoneyTransferCommand, MoneyTransferCommandException
from Repository.Memory_Account_Repository import MemoryAccountRepository


class MoneyTransferUseCase:
    def __init__(self):
        self.accounts_repository = MemoryAccountRepository()
        self.transactions_repository = MemoryTransactionRepository()

    def transfer(self, command_transfer: MoneyTransferCommand):
        a_account = self.accounts_repository.find_by_account_number(command_transfer.a_account_number)
        b_account = self.accounts_repository.find_by_account_number(command_transfer.b_account_number)
        if a_account is None or b_account is None:
            raise TransferUseCaseException("number account has not found")
        transaction = Transaction(
            a_account,
            b_account,
            command_transfer.money_amount)
        self.transactions_repository.insert_transaction(transaction)
        transaction.transfer()
        self.transactions_repository.status_update(transaction.uuid, transaction.status)


class TransferUseCaseException(MoneyTransferCommandException):
    def __init__(self, message):
        self.message = message