from Money_Transfer_Command import MoneyTransferCommand


# import Money_Transfer_Command

class MoneyTransferUseCase:
    def __init__(self, accounts_data_base):
        self.accounts_data_base = accounts_data_base

    def transfer(self, command_transfer:MoneyTransferCommand):
        if command_transfer.a_account_number not in self.accounts_data_base or command_transfer.b_account_number not in self.accounts_data_base:
            raise Exception("number account has not found")
        if self.accounts_data_base[command_transfer.a_account_number].balance < command_transfer.money_amount:
            raise Exception (f"Not enough money to transfer! Your current account balnce: {self.accounts_data_base[command_transfer.a_account_number].balance}")
        if self.accounts_data_base[command_transfer.a_account_number].open_transaction is not None or self.accounts_data_base[command_transfer.b_account_number].open_transaction is not None:
            raise Exception("Account has been blocked")
        self.accounts_data_base[command_transfer.a_account_number].sub_money(command_transfer.money_amount)
        self.accounts_data_base[command_transfer.b_account_number].add_money(command_transfer.money_amount)




#     czy konta nie sa zablokowane
#
