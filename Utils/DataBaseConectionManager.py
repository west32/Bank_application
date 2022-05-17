from flask_mysqldb import MySQL

class DataBaseConectionManagerMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]

class DataBaseConectionManager(metaclass=DataBaseConectionManagerMeta):

    def __init__(self):
        self.mysql = MySQL()

    def get_cursor(self):
        return self.mysql.connection.cursor()

