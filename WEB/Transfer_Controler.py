from flask import Flask

# TODO
# 1. stworzyc endpoint
# 2. w parametrach requesta GET (acount a, acount b i kowta)
# 3. zvalidowac endpoint (sprawdzic czy acount a nie jest pusty itp) np: GET http://localhost:8080/?page_number=100 tutaj page_number=100 to bedzie jeden z paramterow - to jest opcja a a mozliwe 2 opcje ( 2 opcja to wyslac body i w body wpisac parametry a,b accounts i kwote) musze wybrac lepsza opcje. przemyslec jaka metode bede slal i w zwiazku z tym ktora z opcji wybrac zeby bylo lepiej (przeczytaj bykowskiego i consdatatech i flask documentation)
# 4. zaprojektowac klase odpowiedzi powinna zawierac status czy operacja sie powiodla jesli sie nie powiodla to lecii exeption
# 5.z updatowac notatki w readme.md na githubie
# 6.

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/transfer')
def transfer(a_account, b_account, money_amount):
    use_case = Money_Transfer_Usecase.MoneyTransferUseCase(repo)
    command_a = MoneyTransferCommand(a_account, b_account, money_amount)
    use_case.transfer(command_a)
