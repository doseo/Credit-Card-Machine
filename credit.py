#Dongmin Seo

class Account:
	
	
        account = 0 

        due_date = 30 

        def __init__(self, apr, lim):
		Account.account = Account.account+1
		self.apr = apr
		self.lim = lim
		self.dayPrin = {}
		self.bal_sheet = {}
		self.Converter(self.apr)

        #withdrawing the money

	def withdraw(self,amt,day):
		day = self.new(day)
		self.bal_sheet[day] = amt

	#paying money to account

	def pay(self,amt_pay,day):
		day=self.new(day)
		if amt_pay > 0:
			amt_pay=amt_pay*-1
		if amt_pay < 0:
			self.bal_sheet[day] = amt_pay


	#Annual Percentage Rate Calculator

	def apr_calc(self,bal_sheet, dayPrin):
		a = 0
		x=bal_sheet.keys()
		x.sort()
		
		for i in range(len(x)):
			
			if len(x)==1:
				a=a+self.formula(dayPrin[x[i]],self.apr,Account.due_date-x[i])
			elif (i+1)<len(x):
				a=a+self.formula(dayPrin[x[i]],self.apr,x[i+1]-x[i])
			else:
				a=a+self.formula(dayPrin[x[i]],self.apr,Account.due_date-x[i])
		return a

	#last Five Balances

	def get_final_prin_bal(self,dayPrin):
		x = self.dayPrin.keys()
		x.sort()
		return self.dayPrin[x[-1]]


        #given from the scenario
	
        def formula(self,amt_owe, apr, days):
		return ((amt_owe*apr)/365)*days

	#calculates the amount from each transactions

	def calculate(self,bal_sheet,dayPrin):
		a = 0
		for key in sorted(self.bal_sheet):
			a = a+bal_sheet[key]
			self.dayPrin[key] = a

	#Day 1 is counted as zero

	def new(self,day):
		if day==1:
			return 0
		else:
			return day
	
	#Converter

	def Converter(self,apr):
		if self.apr < 1 and self.apr > 0:
			self.apr = self.apr
		elif "%" in str(self.apr):
			self.apr = float(self.apr.strip('%')) / 100.0
		else:
			self.apr = (self.apr)/100.0

