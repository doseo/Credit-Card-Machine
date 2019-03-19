#Dongmin Seo

from credit import Account

def main():

#Test Scenario 1
##A customer opens a credit card with a $1,000.00 limit at a 35% APR.
##The customer charges $500 on opening day (outstanding balance becomes $500).
##The total outstanding balance owed 30 days after opening should be $514.38.
##500 * (0.35 / 365) * 30 = 14.38

        test = Account(0.35,1000)

        test.withdraw(500,1)

        test.calculate(test.bal_sheet,test.dayPrin)

        interest=test.apr_calc(test.bal_sheet,test.dayPrin)

	total=test.get_final_prin_bal(test.dayPrin)+interest

	print "#1:"
	print "Interest: $%05.2f"%(interest)
	print "Total: $%06.2f"%(total)

#Test Scenario 2
##A customer opens a credit card with a $1,000.00 limit at a 35% APR.
##The customer charges $500 on opening day (outstanding balance becomes $500).
##15 days after opening, the customer pays $200 (outstanding balance becomes $300).
##25 days after opening, the customer charges another $100 (outstanding balance becomes $400).
##The total outstanding balance owed 30 days after opening should be $411.99.
##(500 * 0.35 / 365 * 15) + (300 * 0.35 / 365 * 10) + (400 * 0.35 / 365 * 5) = 11.99

	test2 = Account("35%",1000)

	test2.withdraw(500,1)

	test2.pay(200,15)

	test2.withdraw(100,25)
	
	test2.calculate(test2.bal_sheet,test2.dayPrin)

	interest2=test2.apr_calc(test2.bal_sheet,test2.dayPrin)

	total2=test2.get_final_prin_bal(test2.dayPrin)+interest2

	print "\n#2:"
	print "Interest: $%05.2f"%(interest2)
	print "Total: $%06.2f"%(total2)

if __name__=="__main__":
        main()

