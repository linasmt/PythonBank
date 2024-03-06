class Account:
    def __init__(self, number_account, first_deposit=0):
        self.number_account = self._validate_account_number(number_account)
        self.amount = first_deposit

    def _validate_account_number(self, account_number):
        if len(account_number) != 13 or not account_number.isdigit():
            raise ValueError("Account number must be 13 number")
        return account_number

    def check_amount(self):
        return self.amount

    def make_deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.amount += amount
    
    def check_balance(self, user, amount):
        if (self.amount + amount < 0):
            return "false"
        else:
            return "true"
        return "User not found"
