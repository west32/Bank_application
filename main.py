from Business_classes.Money_Transfer_Command import MoneyTransferCommand
from Business_classes.Money_Transfer_Usecase import MoneyTransferUseCase
from Domain_classes.Account import Account


def run_main():
    repo = {
        "123": Account('123', 'Bartek', 444),
        "456": Account('456', 'Łukasz', 0)
    }
    use_case = MoneyTransferUseCase(repo)
    command = MoneyTransferCommand("123", "456", 100)
    use_case.transfer(command)


if __name__ == "__main__":
    run_main()
