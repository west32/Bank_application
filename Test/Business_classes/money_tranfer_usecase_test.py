import unittest
from Domain_classes.Account import Account
from Domain_classes.Transaction import Transaction
from Business_classes.Money_Transfer_Usecase import MoneyTransferUsecase
from Business_classes.Money_Transfer_Command import MoneyTransferCommand

class MoneyTransferUseCaseTest(unittest.TestCase):

    repo={
        "123": Account('123','Bartek',444),
        "456": Account('456','Łukasz',0)
    }

    def test_one_account_locked(self):
        # Given
        self.repo["123"]=Account('123','Bartek',444,'354')
        usecase= MoneyTransferUsecase(self.repo)
        # When
        comamnd= MoneyTransferCommand('123','456',222)
        # Then
        with self.assertRaises(Exception):
            usecase.transfer(comamnd)


            # pozostałe przypadki, pusty numer konta itp



