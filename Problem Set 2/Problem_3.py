#bisect Method

Monthlyinterestrate= (annualInterestRate) / 12.0
Monthlypaymentlowerbound = balance / 12
Monthlypaymentupperbound = (balance * ((1 + Monthlyinterestrate)**12)) / 12.0
for N in range(60):
  #function(lower_bound)
  Minimummonthlypayment = Monthlypaymentlowerbound
  Previousbalance=balance
  for month in range (1,13):
       Monthlyunpaidbalance = (Previousbalance) - (Minimummonthlypayment)
       Updatedbalanceeachmonth = (Monthlyunpaidbalance) + (Monthlyinterestrate * Monthlyunpaidbalance)
       Previousbalance=Updatedbalanceeachmonth
  fa=Updatedbalanceeachmonth    
  #function(upper_bound)    
  Minimummonthlypayment = Monthlypaymentupperbound       
  Previousbalance=balance
  for month in range (1,13):
       Monthlyunpaidbalance = (Previousbalance) - (Minimummonthlypayment)
       Updatedbalanceeachmonth = (Monthlyunpaidbalance) + (Monthlyinterestrate * Monthlyunpaidbalance)
       Previousbalance=Updatedbalanceeachmonth       
  fb=Updatedbalanceeachmonth
  #c ← (a + b)/2
  midpoint = (Monthlypaymentlowerbound+Monthlypaymentupperbound)/2.0  
  #function(midpoint)
  Minimummonthlypayment = midpoint
  Previousbalance=balance
  for month in range (1,13):
       Monthlyunpaidbalance = (Previousbalance) - (Minimummonthlypayment)
       Updatedbalanceeachmonth = (Monthlyunpaidbalance) + (Monthlyinterestrate * Monthlyunpaidbalance)
       Previousbalance=Updatedbalanceeachmonth
  fc=Updatedbalanceeachmonth
  check=(Monthlypaymentupperbound-Monthlypaymentlowerbound)/2 
  #check
  if fc ==0 or check<0.01 :
        break
  #If sign(f(c)) = sign(f(a)) then a ← c else b ← c
  if (fc> 0 and fa> 0) or (fc< 0 and fa< 0) :
       Monthlypaymentlowerbound=midpoint 
  else:
        Monthlypaymentupperbound=midpoint
print('Lowest Payment:',round(Minimummonthlypayment,2))
 
