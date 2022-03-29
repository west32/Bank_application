from flask import Blueprint, jsonify
from Repository.Memory_Account_Repository import MemoryAccountRepository

accounts = Blueprint('accounts', __name__)


@accounts.get('/accounts')
def accounts_repo():
    accounts_dict = MemoryAccountRepository()
    value = accounts_dict.get_all()

    return jsonify(accounts=[account.serialize() for account in value])


