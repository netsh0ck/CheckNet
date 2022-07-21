import datetime
history = {}
class Account(object):
	def __init__(self):
		self.pin = 1234

	def checkCode(self,value):
		return self.pin == value

	def checkBalance(self):
		print 'Current balance is ' + str(self.balance) + ' euros.'

	def checkTransactions(self):
		print 'Previous transactions:'
		for item in sorted(history):
			print item + '\t\t' + str(history[item]) + ' euros.'

	def withdraw(self, pin, value):
		if self.checkCode(pin):
			if value <= self.balance:
				currentTime = datetime.datetime.now()
				history[str(currentTime)] = -value
				self.balance -= value
				print 'Successfully withdrawn ' + str(value) + ' euros from your account.'
			else:
				print 'Not enough balance.'
		else:
			print 'Wrong pin code. Try again.'

	def deposit(self, pin, value):
		if self.checkCode(pin):
			self.balance += value
			history[str(datetime.datetime.now())] = '+' + str(value)
			print 'Successfully deposited ' + str(value) + ' euros from your account.'
		else:
			print 'Wrong pin code. Try again.'

	def createMBNet(self, value):
		import random
		self.MBalance = value
		print 'You have Successfully created an MBNet card with ' + str(self.MBalance) + ' euros.'
		card_ID = [random.randint(0, 9) for _ in xrange(23)]
		print 'Your card id is ' + "".join(str(id) for id in card_ID)
		card_secret = [random.randint(0, 9) for _ in xrange(4)]
		print 'Your secret code is ' + "".join(str(secret) for secret in card_secret)

	def changePIN(self, oldvalue, newvalue):
		if self.checkCode(oldvalue):
			self.pin = newvalue
			print 'Pin code has been successfully changed.'
		else:
			print 'Wrong pin code. Try again.'


class CheckingAccount(Account):
	def __init__(self):
		super(CheckingAccount, self).__init__()
		self.balance = 12000


class SavingsAccount(Account):
	def __init__(self):
		super(SavingsAccount, self).__init__()
		self.balance = 5000
	

class BusinessAccount(Account):
	def __init__(self):
		super(BusinessAccount, self).__init__()
		self.balance = 10000

checksAcc = CheckingAccount()
print 'Enter pin:'
pin = raw_input()
if checksAcc.checkCode(int(pin)):
	checksAcc.withdraw(1234,4000)
	checksAcc.deposit(1234,22000)
	checksAcc.withdraw(1234,22000)
	checksAcc.deposit(1234,24000)
	checksAcc.withdraw(1234,2000)
	checksAcc.deposit(1234,1000)
	checksAcc.withdraw(1234,2000)
	checksAcc.deposit(1234,9000)
checksAcc.checkTransactions()
checksAcc.checkBalance()
myAcc = SavingsAccount()
hisAcc = BusinessAccount()
checksAcc.createMBNet(500)
checksAcc.changePIN(1234, 5678)
