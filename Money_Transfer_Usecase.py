from Money_Transfer_Command import MoneyTransferCommand


# import Money_Transfer_Command

class MoneyTransferUseCase:
    def __init__(self, accounts_data_base):
        self.accounts_data_base = accounts_data_base

    def transfer(self, command_transfer:MoneyTransferCommand):
        if self.accounts_data_base[command_transfer.a_account_number].balance < command_transfer.money_amount:
            raise Exception (f"Not enough money to transfer! Your actual account balnce: {self.accounts_data_base[command_transfer.a_account_number].balance}")
        self.accounts_data_base[command_transfer.a_account_number].sub_money(command_transfer.money_amount)
        self.accounts_data_base[command_transfer.b_account_number].add_money(command_transfer.money_amount)



#     czy kwota przelewu nie jest wieksza niz stan konta z ktorego przelewamy
#     czy konta nie sa zablokowane
#       czy konto istenieje w repo.
