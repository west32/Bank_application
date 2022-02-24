from Money_Transfer_Command import MoneyTransferCommand
from Domain_classes.Account import Account

class MoneyTransferUseCase:
    def __init__(self, accounts_data_base):
        self.accounts_data_base = accounts_data_base

    def transfer(self, command_transfer: MoneyTransferCommand):
        print( self.accounts_data_base[command_transfer.a_account_number])



#     czy kwota przelewu nie jest wieksza niz stan konta z ktorego przelewamy
#     czy konta nie sa zablokowane
#       czy konto istenieje w repo.
