class MoneyTransferUseCase:
    def __init__(self, accounts_data_base=None):
        if accounts_data_base is None:
            accounts_data_base = {}
        self.accounts_data_base = accounts_data_base

    def transfer(self, command_transfer):
        pass

#     czy kwota przelewu nie jest wieksza niz stan konta z ktorego przelewamy
#     czy konta nie sa zablokowane
#       czy konto istenieje w repo.
