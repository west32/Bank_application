class MoneyTransferCommand:
    def __init__(self, a_account_number, b_account_number, money_amount):
        self.a_account_number = a_account_number
        self.b_account_number = b_account_number
        self.money_amount = money_amount
        self.is_number_account_valid()
        self.is_money_amount_greater_than_0()

    def is_number_account_valid(self):
        if self.a_account_number is None or self.b_account_number is None:
            raise Exception("account number is empty")
        elif self.a_account_number == "" or self.b_account_number == "":
            raise Exception("missing number account")

    def is_money_amount_greater_than_0(self):
        if self.money_amount <= 0:
            raise Exception("Transfer money amount have to be grater than 0")
