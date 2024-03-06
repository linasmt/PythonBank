from Bank import Bank
from User import User


if __name__ == '__main__':
    bank1 = Bank("BNP Paribas")
    user1 = User("Kylian Mbappé", "AAOOEF14C")

    bank1.registerUser(user1)
    print(vars(bank1))
    print(vars(user1))

