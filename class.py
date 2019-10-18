class BankAccount:
	def __init__(self, name, balance=0.0):
		self.log("Account is created!")
		self.name=name
		self.balance = balance

	def getBalance(self):
		self.log("Balance checked at" + str(self.balance))
		return self.balance

	def deposit (self, amount):
		self.balance += amount
		self.log("+" + str(amount) + ":" + str(self.balance))

	def withdraw(self, amount):
		self.balance -= amount
		self.log("-" + str(amount) + ":" + str(self.balance))

	def log(self, message):
		print(message)

my_bank_account = BankAccount("Jirayr Melikyan")
my_bank_account.deposit(20.0)
my_bank_account.getBalance()
my_bank_account.withdraw(10.0)
my_bank_account.getBalance()




