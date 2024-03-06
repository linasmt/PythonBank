from Account import Account
from AccountEpargne import AccountEpargne
from AccountCourant import AccountCourant

class User:
    def __init__(self, username):
        self.username = self._validate_username(username)
        self.accounts = []

    def openAccount(self, type_account, account_number, first_depot=0):
        if (type_account == "epargne") :
            new_account = AccountEpargne(account_number, first_depot)
        elif (type_account == "courant"):
            new_account = AccountCourant(account_number, first_depot)
        else:
            print("Invalid account type")
            return false
        self.accounts.append(new_account)
        

    def _validate_username(self, username):
        if not username:
            raise ValueError("Username cannot be empty")
        return username

