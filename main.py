from Business_classes.Money_Transfer_Command import MoneyTransferCommand
from Business_classes.Money_Transfer_Usecase import MoneyTransferUsecase,generate_accounts
from Domain_classes.Account import Account
# if __name__ == '__main__':
# #     Tworzymy instancje klasy MoneyTranferUseCase
# #     Tworzymy instancje klasy MoneyTranferCommand
# #     wywołuje na instancji MoneyTranferUseCase metode MoneyTransferUseCase.transfer(command)
#
# V= MoneyTranferCommand(konta a, b, kwota)
#
# USecase= MoneyTranferUseCase(lista kont)
#
# USecase.trasfer(V)
#
# # unittest na transferze= czy dane konto istenije

def run_main():
    repo={
        "123": Account('123','Bartek',444),
        "456": Account('456','Łukasz',0)
    }
    usecase = MoneyTransferUsecase(repo)
    command = MoneyTransferCommand("123","456",100)
    usecase.transfer(command)



if __name__ == "__main__":
    run_main()
