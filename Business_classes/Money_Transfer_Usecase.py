import random
from Domain_classes.Account import Account,generate_account


def generate_accounts(number_of_accounts):
    accounts_repository = {}
    for _ in range(number_of_accounts):
        random_list = [random.randint(0, 9) for number in range(26)]
        str_account_number = ""
        for number in random_list:
            str_account_number += str(number)

        account = generate_account()

        accounts_repository[account.account_id] = account
    return accounts_repository

repo= generate_accounts(10)
print(repo)

class MoneyTransferUsecase():
    def __init__(self, accounts_data_base=None):
        if accounts_data_base is None:
            accounts_data_base= {}
        self.accounts_data_base = accounts_data_base









    def transfer(self,command_tranfer):
        pass

