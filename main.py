from flask import Flask

from Domain.Account import Account
from WEB.Transfer_Controller import transfers
from WEB.Account_Controller import accounts
from WEB.Transaction_Controller import transactions
from Repository.Memory_Account_Repository import MemoryAccountRepository
from Repository.Memory_Transaction_Repository import MemoryTransactionRepository

account_repository = MemoryAccountRepository()
transaction_repository = MemoryTransactionRepository()
account_repository.up_in(Account('123', 'Bartek', 444))
account_repository.up_in(Account('456', 'Michal', 0))
account_repository.up_in(Account('789', 'Lukasz', 333))


app = Flask(__name__)
app.register_blueprint(transfers)
app.register_blueprint(accounts)
app.register_blueprint(transactions)
app.run(debug=True)

# TODO
# napisac endpoint ktory zwraca wszystkie transakcje danego konta /accounts/123/transactions
# testcase:
# 1 wywołać endpoint transfer z commandem: a=123 b=789 100zl, a=789 b=456 200zl
# 2 wywołać endpoint /accounts/123/transactions i /accounts/456/transactions
# ten endpoint ma zwracac taka strukture
# [
#   {
#       "id": "{uuid}",
#       "date": "26.03.2022",
#       "a_account": "{account_uuid}",
#       "b_account": "{account_uuid}",
#       "status": "{status}"
#   }
# ]