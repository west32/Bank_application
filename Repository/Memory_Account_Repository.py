import uuid
from Domain.Account import Account


class MemoryAccountRepositoryMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]


class MemoryAccountRepository(metaclass=MemoryAccountRepositoryMeta):
    _accounts = {}

    def get_all(self):
        return self._accounts.values()

    def find_by_account_number(self, account_number: str):
        for account in self._accounts.values():
            if account.account_number == account_number:
                return account
        raise AccountRepositoryException(" Account not found")

    def up_in(self, account: Account):
        id = account.id
        if id is not None and id not in self._accounts:
            raise AccountRepositoryException(" Account not found")
        elif id is None:
            id = uuid.uuid4()
            account.id = id
        self._accounts[id] = account

    def delete(self, account_number: str):
        account = self.find_by_account_number(account_number)
        del self._accounts[account.id]


class AccountRepositoryException(Exception):
    def __init__(self, message):
        self.message = message
