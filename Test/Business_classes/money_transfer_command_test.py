import unittest

from Domain.Account import Account
from Service.Money_Transfer_Command import MoneyTransferCommand


class MoneyTransferCommandTest(unittest.TestCase):
    repo = {
        "123": Account('123', 'Bartek', 444),
        "456": Account('456', 'Łukasz', 0),
        "789": Account('789', 'Michał', 60)}

    def test_one_account_number_empty(self):
        with self.assertRaises(Exception):
            MoneyTransferCommand("123", "", 100)

    def test_one_account_number_None(self):
        with self.assertRaises(Exception):
            MoneyTransferCommand(None, "456", 123)

    def test_money_amount_is_None(self):
        with self.assertRaises(Exception):
            MoneyTransferCommand("123", "456", None)

    def test_negative_money_amount(self):
        with self.assertRaises(Exception):
            MoneyTransferCommand("123", "456", -10)

    def test_zero_money_amount(self):
        with self.assertRaises(Exception):
            MoneyTransferCommand("123", "456", 0)

    def test_command_object_valid(self):
        MoneyTransferCommand("123", "456", 19)
