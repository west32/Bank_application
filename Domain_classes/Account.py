import random

class Account():
    def __init__(self, account_id,name,balance:int, open_transaction=None):
        self.account_id = account_id
        self.name = name
        self.open_transaction = open_transaction
        self.balance = balance

    def __str__(self):
        return f" numer konta:{self.account_id}, imie:{self.name}, saldo:{self.balance} złotych"

    def add_money(self):
        pass




    def sub_money(self):
        pass


    def block_account(self,transfer_id):
        # if open_transaction not null throw exeption
        pass

    def unlock_account(self,tranfer_id):
        pass


names= ["Kasia","Bartek","Magda","Maja","Tomek","Michał","Łukasz","Martyna"]

def generate_account():
    random_list = [random.randint(0, 9) for number in range(26)]
    str_account_number = ""
    for number in random_list:
        str_account_number += str(number)
    int_account_number = int(str_account_number)
    name= random.choice(names)
    balance= random.randint(-100,9999)
    user_account=Account(int_account_number,name,balance)
    return user_account

konto= generate_account()

print(konto)