from flask import Blueprint, jsonify,Flask
from flask_mysqldb import MySQL
from Repository.Database_Accounts_Repository import DataBaseAccountRepository
app = Flask(__name__)
mysql = MySQL(app)

accounts = Blueprint('accounts', __name__)


@accounts.get('/accounts')
def accounts_repo():
    accounts_list = DataBaseAccountRepository()
    value = accounts_list.get_all()

    return jsonify(accounts=[account.serialize() for account in value])
