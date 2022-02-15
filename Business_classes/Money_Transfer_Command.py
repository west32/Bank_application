class MoneyTransferCommand():
    def __init__(self,a_account_number,b_account_number,money_amount):
        self.a_account_number = a_account_number
        self.b_account_number = b_account_number
        self.money_amount = money_amount
        self.is_number_account_valid()


    def is_number_account_valid(self):
        if self.a_account_number is None or self.b_account_number is None:
            raise Exception("pusty numer konta")
