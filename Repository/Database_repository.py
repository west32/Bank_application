from Domain.Account import Account
from flask.

class DatabaseAccountRepositoryMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]

class DatabaseAccountRepository(metaclass=DatabaseAccountRepositoryMeta):

    def