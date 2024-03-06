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