import unittest
from Domain_classes.Account import Account
from Business_classes.Money_Transfer_Usecase import MoneyTransferUseCase
from Business_classes.Money_Transfer_Command import MoneyTransferCommand


class MoneyTransferUseCaseTest(unittest.TestCase):
    repo = {
        "123": Account('123', 'Bartek', 444),
        "456": Account('456', 'Łukasz', 0),
        "789": Account('789', 'Michał', 60)
    }

    def test_one_account_locked(self):
        # Given
        self.repo["123"] = Account('123', 'Bartek', 444, '354')
        use_case = MoneyTransferUseCase(self.repo)
        # When
        command = MoneyTransferCommand('123', '456', 222)
        # Then
        with self.assertRaises(Exception):
            use_case.transfer(command)

    def test_one_account_no_money(self):
        self.repo["123"] = Account("123", "Bartek", 50)
        self.repo["456"] = Account("456", "Lukasz", 0)
        use_case = MoneyTransferUseCase(self.repo)
        command = MoneyTransferCommand("456", "123", 100)
        with self.assertRaises(Exception):
            use_case.transfer(command)

    def test_two_accaunts_valid(self):
        self.repo["123"] = Account("123", "Bartek", 444)
        self.repo["456"] = Account("456", "Lukasz", 0)
        use_case = MoneyTransferUseCase(self.repo)
        command = MoneyTransferCommand("123", "456", 100)
        use_case.transfer(command)
        self.assertEqual(self.repo["123"].balance, 344)

    def test_two_accounts_locked(self):
        self.repo["123"] = Account('123', 'Bartek', 444, '456')
        self.repo["456"] = Account('456', 'Łukasz', 0, '123')
        use_case = MoneyTransferUseCase(self.repo)
        command = MoneyTransferCommand('123', '456', 222)
        with self.assertRaises(Exception):
            use_case.transfer(command)