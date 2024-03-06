class User:
    def __init__(self, username, numero_compte, first_depot=0):
        self.username = username
        self.numero_compte = numero_compte
        self.somme = first_depot