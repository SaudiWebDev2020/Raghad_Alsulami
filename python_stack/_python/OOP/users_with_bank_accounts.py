from bank_account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = { 1: BankAccount(int_rate=0.02, balance=0),
                        2: BankAccount(int_rate=0.02, balance=0) }

    def make_deposit(self, amount, account_number):
        self.accounts[account_number].deposit(amount)		
        print(self.accounts[account_number].display_account_info)

    def make_withdrawal(self, amount, account_number):
        self.accounts[account_number].withdraw(amount)		
        print(self.accounts[account_number].display_account_info)
    
    def display_user_balance(self, account_number):
        print(f'User: {self.name}, Account: {account_number}, Balance: {self.accounts[account_number].balance}')


user1 = User('Huda', 'x@gmail.com')
user2 = User('Ahmed', 'x@gmail.com')
user3 = User('Asma', 'x@gmail.com')

user1.make_deposit(1000,2)
user1.make_deposit(2000,1)
user1.make_withdrawal(500,1)
user1.display_user_balance(1)
user1.display_user_balance(2)

user2.make_deposit(2000,1)
user2.make_withdrawal(700,1)
user2.make_withdrawal(50,2)
user2.display_user_balance(1)
user2.display_user_balance(2)

user3.make_deposit(4000,1)
user3.make_withdrawal(700,1)
user3.make_withdrawal(1000,2)
user3.display_user_balance(1)
user3.display_user_balance(2)