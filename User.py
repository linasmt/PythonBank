class User:
    def __init__(self, username, account_number, first_depot=0):
        self.username = self._validate_username(username)
        self.account_number = self._validate_account_number(account_number)
        self.sum = first_depot

    def _validate_username(self, username):
        if not username:
            raise ValueError("Username cannot be empty")
        return username

    def _validate_account_number(self, account_number):
        if len(account_number) != 13:
            raise ValueError("Account number must be 10 number")
        return account_number
