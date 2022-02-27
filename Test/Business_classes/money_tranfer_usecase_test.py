import unittest
from Account import Account
from Money_Transfer_Usecase import MoneyTransferUseCase
from Money_Transfer_Command import MoneyTransferCommand


class MoneyTransferUseCaseTest(unittest.TestCase):
    repo = {
        "123": Account('123', 'Bartek', 444),
        "456": Account('456', 'Łukasz', 0),
        "789": Account('789', 'Michał', 60),
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
        command = MoneyTransferCommand("123", "456", 100)
        with self.assertRaises(Exception):
            use_case.transfer(command)
        command = MoneyTransferCommand("123", "456", 50)
        use_case.transfer(command)

    def test_two_accounts_valid(self):
        self.repo["123"] = Account("123", "Bartek", 444)
        self.repo["456"] = Account("456", "Lukasz", 0)
        use_case = MoneyTransferUseCase(self.repo)
        command = MoneyTransferCommand("123", "456", 100)
        use_case.transfer(command)
        self.assertEqual(self.repo["123"].balance, 344)
        self.assertEqual(self.repo["456"].balance, 100)

    def test_two_accounts_locked(self):
        self.repo["123"] = Account('123', 'Bartek', 444, '456')
        self.repo["456"] = Account('456', 'Łukasz', 0, '123')
        use_case = MoneyTransferUseCase(self.repo)
        command = MoneyTransferCommand('123', '456', 222)
        with self.assertRaises(Exception):
            use_case.transfer(command)

    # TODO  move to command_test
    # def test_one_account_balance_is_None(self):
    #     self.repo["123"] = Account("123", "Bartek",444)
    #     use_case = MoneyTransferUseCase(self.repo)
    #     command = MoneyTransferCommand("123", "456", None)
    #     use_case.transfer(command)
    #     with self.assertRaises(Exception):
    #         use_case.transfer(command)

    # TODO MOVE TO money_tranfer_command_test
    # def test_one_account_number_empty(self):
    #     self.repo["123"] = Account("123", "Bartek", 50)
    #     self.repo["456"] = Account("456", "Lukasz", 0)
    #     use_case = MoneyTransferUseCase(self.repo)
    #     command = MoneyTransferCommand("123", "", 100)
    #     with self.assertRaises(Exception):
    #         use_case.transfer(command)

    # TODO MOve to Money_tranfer_commnad_test
    # def test_one_account_number_is_None(self):
    #     self.repo["123"] = Account("123", "Bartek", 50)
    #     self.repo["456"] = Account("456", "Lukasz", 0)
    #     use_case = MoneyTransferUseCase(self.repo)
    #     command = MoneyTransferCommand(a_account_number="123", b_account_number=None, money_amount=100)
    #     with self.assertRaises(Exception):
    #         use_case.transfer(command)

    # TODO move to Money_command_test
    # def test_negative_money_amount(self):
    #     self.repo["123"] = Account("123", "Bartek", 444)
    #     self.repo["456"] = Account("456", "Lukasz", 0)
    #     use_case = MoneyTransferUseCase(self.repo)
    #     command = MoneyTransferCommand("123", "456", -10)
    #     with self.assertRaises(Exception):
    #         use_case.transfer(command)

    # TODO move to money_transfer_command_test
    # def test_zero_money_amount(self):
    #     self.repo["123"] = Account("123", "Bartek", 444)
    #     self.repo["456"] = Account("456", "Lukasz", 0)
    #     use_case = MoneyTransferUseCase(self.repo)
    #     command = MoneyTransferCommand("123", "456", 0)
    #     with self.assertRaises(Exception):
    #         use_case.transfer(command)
