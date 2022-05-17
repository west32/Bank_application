from flask import Flask, jsonify
from flask_mysqldb import MySQL
from Domain.Account import Account
from Utils.DataBaseConectionManager import DataBaseConectionManager

class DataBaseAccountRepositoryMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]

class DataBaseAccountRepository(metaclass=DataBaseAccountRepositoryMeta):

    @staticmethod
    def _get_cursor():
        db = DataBaseConectionManager()
        return db.get_cursor()

    def get_all(self):
        cur = self._get_cursor()
        cur.execute("""SELECT * FROM `account` """)
        rv = cur.fetchall()
        accounts_list = []
        for element in rv:
            account = Account(account_number=element[1],
                              name=element[2],
                              balance=element[3],
                              id=element[0])
            accounts_list.append(account)
        return accounts_list

