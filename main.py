from Service.Money_Transfer_Command import MoneyTransferCommand
from Service import Money_Transfer_Usecase
from Domain.Account import Account


def run_main():
    repo = {
        "123": Account('123', 'Bartek', 444, ),
        "456": Account('456', 'Łukasz', 0),
        "789": Account('789', 'Michał', 300, open_transaction="123")
    }
    use_case = Money_Transfer_Usecase.MoneyTransferUseCase(repo)
    command_a = MoneyTransferCommand("123", "456", 100)
    command_b = MoneyTransferCommand("456", "123", 50)
    # command_e = MoneyTransferCommand("","456",99)
    # command_e = MoneyTransferCommand("789","123",10)
    # command_e = MoneyTransferCommand("123", "789", 10)
    # command_e = MoneyTransferCommand("532", "123", 10)
    # command_e = MoneyTransferCommand("123", "532", 10)
    # command_e = MoneyTransferCommand('123','456',999)
    # command_e = MoneyTransferCommand('123', None, 29)
    # command_e = MoneyTransferCommand('123',"", 50)
    # command_e = MoneyTransferCommand('123', '456', -29)
    # command_e = MoneyTransferCommand('123', '456', 0)
    use_case.transfer(command_a)
    # use_case.transfer(command_b)
    # use_case.transfer(command_e)



# napisac w metodzie trasfer przed wykonaniem transferu block account
#  i po wykonaniu unlock account


if __name__ == "__main__":
    run_main()
