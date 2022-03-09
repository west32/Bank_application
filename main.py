from flask import Flask

from Domain.Account import Account
from WEB.Transfer_Controller import transfers
from WEB.Account_Controller import accounts
from Repository.Account_Repository import AccountRepository

account_repository = AccountRepository()
account_repository.up_in(Account('123', 'Bartek', 444))
account_repository.up_in(Account('456', 'Michal', 0))
account_repository.up_in(Account('789', 'Lukasz', 333))

app = Flask(__name__)
app.register_blueprint(transfers)
app.register_blueprint(accounts)
app.run(debug=True)
