class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    
    def display_user_balance(self):
        print (f'User: {self.name}, Balance: {self.balance}')
        return self

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        return self


user1 = User('Huda')
user2 = User('Ahmed')
user3 = User('Asma')

user1.make_deposit(1000).make_deposit(2000).make_deposit(1500).make_withdrawal(500).display_user_balance()
user2.make_deposit(2000).make_deposit(2000).make_withdrawal(700).make_withdrawal(1000).display_user_balance()
user3.make_deposit(4000).make_withdrawal(700).make_withdrawal(300).make_withdrawal(1000).display_user_balance()