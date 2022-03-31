import json
import uuid
from Domain.Account import Account


class FileAccountRepositoryMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]


class FileAccountRepository(metaclass=FileAccountRepositoryMeta):


    def load_repo_from_file(self):
        with open ("accounts.bartek", "r", encoding="utf-8") as file:
            accounts_dict = json.load(file)
        return accounts_dict


    def save_repo_to_file(self, accounts_dict):
        with open ("accounts.bartek", "w", encoding="utf-8") as file:
            json.dump(accounts_dict, file, indent=4)

    def get_all(self):
        with open('accounts.bartek', "r", encoding='utf-8') as acc_file:
            accounts_dict = json.load(acc_file)
        return accounts_dict.values()

    def find_by_account_number(self, account_number: str):
        for account in self._accounts.values():
            if account.account_number == account_number:
                return account
        raise AccountRepositoryException(" Account not found")

    def up_in(self, account: Account):
        id = uuid.uuid4()
        account.id = id
        accounts_dict = self.load_repo_from_file()
        print(accounts_dict)

        accounts_dict['accounts'].append(account.serialize())
        self.save_repo_to_file(accounts_dict)
        print(accounts_dict)



        # id = account.id
        # if id is not None and id not in self._accounts:
        #     raise AccountRepositoryException(" Account not found")
        # elif id is None:
        #     id = uuid.uuid4()
        #     account.id = id
        # self._accounts[id] = account

    #
    # def delete(self, account_number: str):
    #     account = self.find_by_account_number(account_number)
    #     with open ("accounts.bartek", "w", encoding="utf-8") as acc_file:
    #         json.
        # del self._accounts[account.id]


class AccountRepositoryException(Exception):
    def __init__(self, message):
        self.message = message
