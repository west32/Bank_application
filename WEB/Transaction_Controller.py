from flask import Blueprint, jsonify
from Repository.Memory_Transaction_Repository import  MemoryTransactionRepository


transactions = Blueprint('transactions', __name__)


@transactions.get('/accounts/123/transactions')
def transactions_repo():
    transactions_dict = MemoryTransactionRepository()
    value = transactions_dict._transactions.values()

    return jsonify(transactions=[transaction.serialize() for transaction in value])
