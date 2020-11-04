class BankAccount:
    def __init__(self, int_rate, balance=0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
		# your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
		# your code here
        if amount < self.balance:
            self.balance -= amount
        else: 
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
		# your code here
        print (f'Balance: ${self.balance}')
        return self

    def yield_interest(self):
		# your code here
        self.balance += self.balance * self.int_rate
        return self


# account1 = BankAccount(10, 1000)
# account2 = BankAccount(5)

# account1.deposit(200).deposit(50).deposit(100).withdraw(300).yield_interest().display_account_info()
# account2.deposit(1800).deposit(70).withdraw(50).withdraw(100).withdraw(50).withdraw(250).yield_interest().display_account_info()