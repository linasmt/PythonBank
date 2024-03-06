class Account:
    def __init__(self, number_account, first_deposit=0):
        self.number_account = number_account
        self.amount = first_deposit
    
    def _validate_account_number(self, account_number):
        if len(account_number) != 13:
            raise ValueError("Account number must be 10 number")
        return account_number
