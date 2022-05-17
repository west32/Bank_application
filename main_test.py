from flask import Flask, jsonify
from flask_mysqldb import MySQL
from Domain.Account import Account

app = Flask(__name__)

# Required
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "dupa123"
app.config["MYSQL_DB"] = "trans_acc"
app.config["MYSQL_PORT"] = 3307


mysql = MySQL(app)

@app.route("/")
def users():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM `account` """)
    rv = cur.fetchall()
    accounts_list = []
    for element in rv:
        account = Account(account_number=element[1],
                                name=element[2],
                                balance=element[3],
                                id=element[0])
        accounts_list.append(account)
    return jsonify(accounts=[account.serialize() for account in accounts_list ])


if __name__ == "__main__":
    app.run(debug=True)


# TODO
# data transfer object
# data acces object
# agregate root
# propozycja refactoringu
#  transactiuon repository databasee na podstawie account