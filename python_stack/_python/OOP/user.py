class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
    
    def make_withdrawal(self, amount):
        self.balance -= amount
    
    def display_user_balance(self):
        return f'User: {self.name}, Balance: {self.balance}'

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount


user1 = User('Huda')
user2 = User('Ahmed')
user3 = User('Asma')

user1.make_deposit(1000)
user1.make_deposit(2000)
user1.make_deposit(1500)
user1.make_withdrawal(500)
print(user1.display_user_balance())

user2.make_deposit(2000)
user2.make_deposit(2000)
user2.make_withdrawal(700)
user2.make_withdrawal(1000)
print(user2.display_user_balance())

user3.make_deposit(4000)
user3.make_withdrawal(700)
user3.make_withdrawal(300)
user3.make_withdrawal(1000)
print(user3.display_user_balance())