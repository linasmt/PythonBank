from Bank import Bank
from User import User


if __name__ == '__main__':
    bank = Bank("BNP Paribas")
    user1 = User("Kylian Mbappé")
    user1.openAccount("courant", "AAOOEF14C", 5)
    user1.openAccount("epargne", "BBFDSG78G", 23)
    user1.showAccounts()
    print(vars(user1))
    bank.registerUser(user1)
    
    bank.registerNewUser("Fabrice éboué", "AACDE18E", 50)
    user2 = bank.getUserByNumeroCompte("AACDE18E")
    
    print(vars(bank))
    print(bank.getSoldeBank())