from User import User

class Bank:
    def __init__(self, name):
        self.name = name
        self.users = []
    
    def registerUser(self, user):
        self.users.append(user)

    def registerNewUser(self, user_name, numero_compte, first_depot = 0):
        new_user = User(user_name, numero_compte, first_depot)
        self.registerUser(new_user)
    
    def getUserByNumeroCompte(self, numero_compte):
        for user in self.users:
            if user.numero_compte == numero_compte:
                return user
        print("No user found.")
        return false
    
    def getSoldeBank(self):
        sum = 0
        for user in self.users:
            sum += user.somme
        return sum
