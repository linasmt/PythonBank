from User import User

class Bank:
    def __init__(self, name):
        self.name = name
        self.users = {}
    
    def registerUser(self, user):
        self.users[user.id_user] = user

    def registerNewUser(self, user_name, id_user, numero_compte, first_depot = 0, type_account="courant"):
        new_user = User(user_name, id_user)
        new_user.openAccount(type_account, numero_compte, first_depot)
        self.registerUser(new_user)
        return new_user
    
    def getUserByID(self, id_user):
        return self.users[id_user]
    
    def getSoldeBank(self):
        sum = 0
        for user in (self.users).values():
            print(user.accounts)
            if len(user.accounts) > 0:
                for account in user.accounts:
                    sum += account.amount
        return sum
