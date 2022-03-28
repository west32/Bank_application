from Domain.Transaction import Transaction
from Domain.Transaction_Status import Status


class MemoryTransactionRepositoryMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]


class MemoryTransactionRepository(metaclass=MemoryTransactionRepositoryMeta):
    _transactions = {}

    def status_update(self, id, status):
        transaction = self._transactions[id]
        if transaction is None:
            raise TransactionRepositoryException("Transaction not found")
        transaction.status = status

    def find_by_account_number(self, account_number: str):
        transactions = []
        for transaction in self._transactions.values():
            if transaction.a_account.account_number == account_number or transaction.b_account.account_number == account_number:
                transactions.append(transaction)
        return transactions

    def insert_transaction(self, transaction: Transaction):
        self._transactions[transaction.uuid] = transaction


class TransactionRepositoryException(Exception):
    def __init__(self, message):
        self.message = message
