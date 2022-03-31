from flask import Blueprint, jsonify
from Repository.Memory_Account_Repository import MemoryAccountRepository
from Repository.File_Accounts_Repository import FileAccountRepository

accounts = Blueprint('accounts', __name__)


@accounts.get('/accounts')
def accounts_repo():
    accounts_dict = FileAccountRepository()
    value = accounts_dict.get_all()

    return jsonify(accounts=[account.serialize() for account in value])


