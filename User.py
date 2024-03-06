from SavingAccount import SavingAccount
from CurrentAccount import CurrentAccount


class User:
    def __init__(self, username, id_user):
        self.username = self._validate_username(username)
        self.id_user = id_user
        self.accounts = []

    def openAccount(self, type_account, account_number, first_depot=0):
        if type_account == "epargne":
            new_account = SavingAccount(account_number, first_depot)
        elif type_account == "courant":
            new_account = CurrentAccount(account_number, first_depot)
        else:
            print("Invalid account type")
            return False
        self.accounts.append(new_account)

    def _validate_username(self, username):
        if not username:
            raise ValueError("Username cannot be empty")
        return username

    def showAccounts(self):
        for account in self.accounts:
            print("Compte " + account.number_account + ": " + str(account.amount) + " €")
