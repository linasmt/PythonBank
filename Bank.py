from User import User


class Bank:
    def __init__(self, name):
        selfusername = name
        self.users = {}

    def registerUser(self, user):
        self.users[user.id_user] = user

    def registerNewUser(self, user_name, id_user, account_number, first_depot=0, type_account="courant"):
        new_user = User(user_name, id_user)
        new_user.openAccount(type_account, account_number, first_depot)
        self.registerUser(new_user)
        return new_user

    def getUserByID(self, id_user):
        if self.users.get(id_user) is not None:
            return self.users[id_user]
        else:
            print("No user found.")
            return False

    def getSoldeBank(self):
        sum = 0
        for user in (self.users).values():
            if len(user.accounts) > 0:
                for account in user.accounts:
                    sum += account.amount
        return sum
    

    def transaction(self, amount_transaction, user_receivedmoney='banque', user_sendmoney='banque', nb_account_reciever="", nb_account_sender=""):
        if user_sendmoney != 'banque':
            self.add_money(user_receivedmoney.id_user, nb_account_reciever, amount_transaction)
            self.withdraw_money(user_receivedmoney, user_sendmoney.id_user, nb_account_sender, amount_transaction)
        else:
            if self.users.get(id_user_sender) is not None:
                bank_user = self.users[id_user_sender]
                for acc in bank_user.accounts:
                    if acc.number_account == nb_account_sender:
                        balance = acc.check_balance(amount_transaction)
                        if balance == "true":
                            acc.amount -= amount_transaction
                            self.log_transaction(u, "true", user)
                        else:
                            self.log_transaction(u, "false", user)
                            return
        return "User not found"

    def log_transaction(self, user, verify, user_sendmoney):
        if verify == "true":
            print(f"Demande Transaction de {user_sendmoney} à {user.username} acceptée")
            print(f"Solde compte en banque après : {user.somme}")
        else:
            print(f"Demande Transaction de {user_sendmoney} à {user.username} refusée")
            print(f"Solde compte en banque après : {user.somme}")

    def add_money(self, id_user, nb_account, amount):
        if self.users.get(id_user) is not None:
            bank_user = self.users[id_user]
            for acc in bank_user.accounts:
                if acc.number_account == nb_account:
                    acc.amount += amount
                    return "Money added"

        return "User not found"

    def withdraw_money(self, id_user_sender, user, nb_account_sender, amount_transaction):
        if self.users.get(id_user_sender) is not None:
            bank_user = self.users[id_user_sender]
            for acc in bank_user.accounts:
                if acc.number_account == nb_account_sender:
                    balance = acc.check_balance(amount_transaction)
                    if balance == "true":
                        acc.amount -= amount_transaction
                        self.log_transaction(u, "true", user)
                    else:
                        self.log_transaction(u, "false", user)
                        return
        return "User not found"
