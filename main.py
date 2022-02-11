from Business_classes.Money_Transfer_Command import MoneyTransferCommand
from Business_classes.Money_Transfer_Usecase import MoneyTransferUsecase,generate_accounts


def run_homework():
    repo = generate_accounts(10)
    usecase = MoneyTransferUsecase(repo)
    command = MoneyTransferCommand(repo[0],repo[4],324)
    usecase.transfer(command)
