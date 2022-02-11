import random
from Domain_classes.Account import Account,generate_account


class MoneyTransferUsecase():
    def __init__(self, accounts_data_base=None):
        if accounts_data_base is None:
            accounts_data_base= {}
        self.accounts_data_base = accounts_data_base


    def generate_accounts(self):

        account= None
        for _ in range(10):
            random_list = [random.randint(0, 9) for number in range(26)]
            str_account_number = ""
            for number in random_list:
                str_account_number += str(number)
            account = generate_account()

            self.accounts_data_base[account.account_id]=account
        return self.accounts_data_base



    def transfer(self,command_tranfer):
        pass

przelew= MoneyTransferUsecase()
przelew.generate_accounts()
print(przelew.accounts_data_base)