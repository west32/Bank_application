from flask import Flask

from Domain.Account import Account
from WEB.Transfer_Controller import transfers
from WEB.Account_Controller import accounts
from WEB.Transaction_Controller import transactions
from Repository.Memory_Account_Repository import MemoryAccountRepository
from Repository.Memory_Transaction_Repository import MemoryTransactionRepository
from Repository.File_Accounts_Repository import FileAccountRepository

account_repository = FileAccountRepository()
transaction_repository = MemoryTransactionRepository()

account_repository.up_in(Account("575", "Kuba", 24))


# account_repository.up_in(Account("123", "Bartek", 1, id="de75bc6d-6a4d-4d78-bafb-a1fcff4d96a8"))


app = Flask(__name__)
app.register_blueprint(transfers)
app.register_blueprint(accounts)
app.register_blueprint(transactions)

app.run(debug=True)

# TODO
# dodaje plik accounts.bartek na nowym branchu do projektu.
# w klasie z repozytoriami tworze nowe repo o nawie FileAccountsRepository
#  tam kopiuje wszystkie motody z klasy memoryaccoyntsrepo, kiedy aplikacja wstaje ja mam z pliku
# kiedy bede wywolywal poszczzehgolne funkcje w tej klasie to one maja otwierac ten plik (wykonywac operacje na tym pliku)
# to samo z transakcjami :D skoro mi tak swietnie idzie :D xDD
#  napisac testy jednostkowe do naszych repozytoriow z plikow i te repozytoria nie byly wpiete do hexa
