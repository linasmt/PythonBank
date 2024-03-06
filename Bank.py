from User import User


class Bank:
    def __init__(self, name):
        self.name = name
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
