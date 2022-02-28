import unittest
from Account import Account
from Money_Transfer_Command import MoneyTransferCommand
from Money_Transfer_Usecase import MoneyTransferUseCase


class MoneyTransferCommandTest(unittest.TestCase):
    repo = {
        "123": Account('123', 'Bartek', 444),
        "456": Account('456', 'Łukasz', 0),
        "789": Account('789', 'Michał', 60),
    }

    def test_one_account_number_empty(self):
        self.repo["123"] = Account("123", "Bartek", 50)
        self.repo["456"] = Account("456", "Lukasz", 0)
        use_case = MoneyTransferUseCase(self.repo)
        command = MoneyTransferCommand("123", "", 100)
        with self.assertRaises(Exception):
            use_case.transfer(command)

    def test_one_account_number_is_None(self):
        self.repo["123"] = Account("123", "Bartek", 50)
        self.repo["456"] = Account("456", "Lukasz", 0)
        use_case = MoneyTransferUseCase(self.repo)
        command = MoneyTransferCommand(a_account_number="123", b_account_number=None, money_amount=100)
        with self.assertRaises(Exception):
            use_case.transfer(command)

    def test_one_account_balance_is_None(self):
        self.repo["123"] = Account("123", "Bartek", 444)
        use_case = MoneyTransferUseCase(self.repo)
        command = MoneyTransferCommand("123", "456", None)
        use_case.transfer(command)
        with self.assertRaises(Exception):
            use_case.transfer(command)

    def test_negative_money_amount(self):
        self.repo["123"] = Account("123", "Bartek", 444)
        self.repo["456"] = Account("456", "Lukasz", 0)
        use_case = MoneyTransferUseCase(self.repo)
        command = MoneyTransferCommand("123", "456", -10)
        with self.assertRaises(Exception):
            use_case.transfer(command)

    def test_zero_money_amount(self):
        self.repo["123"] = Account("123", "Bartek", 444)
        self.repo["456"] = Account("456", "Lukasz", 0)
        use_case = MoneyTransferUseCase(self.repo)
        command = MoneyTransferCommand("123", "456", 0)
        with self.assertRaises(Exception):
            use_case.transfer(command)
