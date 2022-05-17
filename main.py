from flask import Flask
from flask_mysqldb import MySQL
from WEB.Transfer_Controller import transfers
from WEB.Account_Controller import accounts
from WEB.Transaction_Controller import transactions
from Repository.Database_Accounts_Repository import DataBaseAccountRepository
from Utils.DataBaseConectionManager import DataBaseConectionManager

app = Flask(__name__)
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "dupa123"
app.config["MYSQL_DB"] = "trans_acc"
app.config["MYSQL_PORT"] = 3307

db = DataBaseConectionManager()
db.mysql.init_app(app)

app.register_blueprint(transfers)
app.register_blueprint(accounts)
app.register_blueprint(transactions)

if __name__ == "__main__":
    app.run(debug=True)


