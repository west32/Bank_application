from flask import Flask
from flask_mysqldb import MySQL

class DataBaseAccountRepositoryMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]

class DataBaseAccountRepository(metaclass=DataBaseAccountRepositoryMeta):

    def connect(self, app):
        app.config["MYSQL_HOST"] = "127.0.0.1"
        app.config["MYSQL_USER"] = "root"
        app.config["MYSQL_PASSWORD"] = "dupa123"
        app.config["MYSQL_DB"] = "trans_acc"
        app.config["MYSQL_PORT"] = 3307



    def get_all(self):
        pass
