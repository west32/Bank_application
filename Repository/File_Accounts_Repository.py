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
        accounts_list = []
        with open("accounts.bartek", "r", encoding="utf-8") as file:
            dict_list = json.load(file)
            for account in dict_list:
                serialized_account = Account(account_number=account["account_number"],
                                             name=account["name"],
                                             balance=account["account_balance"],
                                             id=account["id"])
                accounts_list.append(serialized_account)
        return accounts_list

    def save_repo_to_file(self, accounts_list):
        serialized_accounts_list=[]
        for account in accounts_list:
            serialized_accounts_list.append(account.serialize())
        with open("accounts.bartek", "w", encoding="utf-8") as file:
            json.dump(serialized_accounts_list, file, indent=4)

    def get_all(self):
        return self.load_repo_from_file()

    def find_by_account_number(self, account_number: str):
        accounts = self.load_repo_from_file()
        for account in accounts:
            if account.account_number == account_number:
                return account
        raise AccountRepositoryException(" Account not found")

    def up_in(self, account: Account):
        accounts_list = self.load_repo_from_file()
        print("asfijj")

        if account.id is None:
            id = uuid.uuid4()
            account.id = id
            if self.find_by_account_number(account.account_number) in accounts_list:
                raise AccountRepositoryException ("no acces to this account")
        else:
            account_pop = False
            for index, account_from_list in enumerate(accounts_list):
                if account.id == account_from_list.id:
                    accounts_list.pop(index)
                    account_pop = True
                    break
            if not account_pop:
                raise AccountRepositoryException("Account not found")
        accounts_list.append(account)
        self.save_repo_to_file(accounts_list)

        # accounts_list = self.load_repo_from_file()
        # if account
        # self.save_repo_to_file(accounts_dict)

        # id = account.id
        # if id is not None and id not in self._accounts:
        #     raise AccountRepositoryException(" Account not found")
        # elif id is None:
        #     id = uuid.uuid4()
        #     account.id = id
        # self._accounts[id] = account

    def delete(self, account_number: str):
        account_to_delete = self.find_by_account_number(account_number)
        account_dict = self.load_repo_from_file()
        for accounts in account_dict.values():
            for account in accounts:
                print(account)
                # if account_to_delete.account_number == account.account_number:
                #     del account_dict[accounts][account]
        # del account_dict.values[account]


class AccountRepositoryException(Exception):
    def __init__(self, message):
        self.message = message
