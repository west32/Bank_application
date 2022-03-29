from flask import Blueprint, jsonify
from Repository.Memory_Transaction_Repository import MemoryTransactionRepository

transactions = Blueprint('transactions', __name__)


@transactions.get('/accounts/<account_number>/transactions')
def transactions_repo(account_number):
    transactions_dict = MemoryTransactionRepository()
    value = transactions_dict.find_by_account_number(account_number)

    return jsonify(transactions=[transaction.serialize() for transaction in value])
