from Account import Account


class SavingAccount(Account):
    def __init__(self, number_account, first_deposit=0):
        Account.__init__(self, number_account, first_deposit)
