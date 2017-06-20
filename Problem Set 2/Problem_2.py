#put any number for balance ,annualInterestRate  to test code
balance = 3329
annualInterestRate = 0.2
Monthlyinterestrate= (annualInterestRate) / 12.0
Minimummonthlypayment = 0
Updatedbalanceeachmonth=1 #to guarantee that it enters loop the first time and it is first random number not less than zero
while Updatedbalanceeachmonth>0:
   Minimummonthlypayment += 10 
   Previousbalance=balance
   for month in range (1,13):
       Monthlyunpaidbalance = (Previousbalance) - (Minimummonthlypayment)
       Updatedbalanceeachmonth = (Monthlyunpaidbalance) + (Monthlyinterestrate * Monthlyunpaidbalance)
       Previousbalance=Updatedbalanceeachmonth
print('Lowest Payment:',Minimummonthlypayment)
  
