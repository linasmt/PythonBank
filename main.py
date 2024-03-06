from Bank import Bank
from User import User

if __name__ == '__main__':
    bank = Bank("BNP Paribas")
    user1 = User("Kylian Mbappé")
    user1.openAccount("courant", "1234567891234", 5)
    user1.openAccount("epargne", "1234567891234", 23)
    user1.showAccounts()
    print(vars(user1))
    bank.registerUser(user1)
    
    bank.registerNewUser("Fabrice éboué", "1234567891234", 50)
    user2 = bank.getUserByNumeroCompte("1234567891234")
    
    print(vars(bank))
    print(bank.getSoldeBank())