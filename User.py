from Account import Account
from AccountEpargne import AccountEpargne
from AccountCourant import AccountCourant

class User:
    def __init__(self, username):
        self.username = username
        self.accounts = []

    def openAccount(self, type_account, numero_account, first_depot=0):
        if (type_account == "epargne") :
            new_account = AccountEpargne(numero_account, first_depot)
        elif (type_account == "courant"):
            new_account = AccountCourant(numero_account, first_depot)
        else:
            print("Invalid account type")
            return false
        self.accounts.append(new_account)