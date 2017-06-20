#Problem 1
#put any number for balance ,annualInterestRate and monthlyPaymentRate in order to test
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
Monthlyinterestrate= (annualInterestRate) / 12.0
Previousbalance=balance
for i in range (1,13): # loop from 1 to 12 as 13(end) is not included .It will iterate 12 times
    Minimummonthlypayment = (monthlyPaymentRate) * (Previousbalance)
    Monthlyunpaidbalance = (Previousbalance) - (Minimummonthlypayment)
    Updatedbalanceeachmonth = (Monthlyunpaidbalance) + (Monthlyinterestrate * Monthlyunpaidbalance)
    Previousbalance=Updatedbalanceeachmonth     
print('Remaining balance:',round(Updatedbalanceeachmonth,2))
