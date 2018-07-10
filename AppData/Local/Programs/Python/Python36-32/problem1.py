balance=int(input("Enter balance"))
annualInterestRate=float(input("Enter interest rate"))
monthlyPaymentRate=float(input("Enter payment rate"))
i=0
mr=annualInterestRate/12.0
while(i<12):
    balance=balance-(balance*monthlyPaymentRate)
    balance=balance+(mr*balance)
    i+=1
print('Remaining balance:',end="")
print('%.2f'%balance)
    
