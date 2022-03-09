from flask import Blueprint, jsonify
from Repository.Account_Repository import AccountRepository


accounts = Blueprint('accounts', __name__)


@accounts.get('/accounts')
def accounts_repo():
    accounts_dict = AccountRepository()
    value = accounts_dict._accounts.values()

    return jsonify(accounts=[account.serialize()for account in value])
















        # value = accounts_asd._accounts.items()
    # json = {}
    # for id, account in value:
    #     json[f"{str(id)[:5]}..."] = (account.name, account.account_number)
    # print(value)
    # print(json)
    # return json
