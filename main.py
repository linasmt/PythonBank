from Bank import Bank
from User import User

if __name__ == '__main__':
    bank = Bank("BNP Paribas")
    user1 = User("Kylian Mbappé", 1)
    user1.openAccount("courant", "1234667897412", 5)
    user1.openAccount("epargne", "1236547896542", 23)
    user1.showAccounts()
    print(vars(user1))
    bank.registerUser(user1)
    
    user2 = bank.registerNewUser("Fabrice éboué", 2, "7418529630458", 50)
    user2.showAccounts()

    print(vars(bank))
    print(bank.getSoldeBank())