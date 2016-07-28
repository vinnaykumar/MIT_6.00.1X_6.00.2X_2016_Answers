
""" Following is a script for Problem Set 02 in Week 02. """

# Using timeit to measure time a program takes to run
from timeit import Timer


balance = 320000          # Delete this variable before pasting into grader
annualInterestRate = 0.2  # Delete this variable before pasting into grader



# Cardsummary
def cardsummary (balance, annualInterestRate, monthlyPaymentRate):

    """ This function calculates
    1. minimum monthly payment,
    2. monthly remainig balance,
    3. total payments made in a year,
    4. remaining balance at the end of the year. """
    

    paymentlist = [] # Empty list to capture all the monthly payments
    
    i = 1
    while i < 13:
        print "Month: " + str(i)

        minpayment = round(balance * monthlyPaymentRate, 2) # Calculating minimum monthly payment rounded to two decimals.
        paymentlist.append(minpayment)
        Totalpayment = sum(paymentlist)
        print "Minimum monthly payment: " + str(minpayment)

        rembalance = balance - minpayment # Calculating monthly remainig balance
        updatedbalance = round(rembalance + ((annualInterestRate / 12.0)*rembalance),2)
        print "Remaining balance: " + str(updatedbalance) + "\n"

        balance = updatedbalance

        i += 1

    print "Total paid: " + str(Totalpayment) # Capturing total payments made in a year
    print "Remainig balance: " + str(updatedbalance) + "\n" # Capturing remainig balance at the end of the year

cardsummary(balance, annualInterestRate, monthlyPaymentRate)



# Paying Debt Off
def returnbalance(balance, fixedsum):

    """ This function return balance at the end of the year
    after paying a fixed sum every month and monthly interest rate applied
    at the end of each month """
    
    i = 1
    while i < 13:
        unpaidbalance = balance - fixedsum
        updatedbalance = unpaidbalance + ((annualInterestRate / 12.0)*unpaidbalance)
        balance = updatedbalance
        i += 1
    return balance



# Paying Debt Off - Bisection Search
def findfixedsumquick (balance, annualInterestRate):

    """ This function finds minimum constant montly payment to be made
    to successfully pay off the debt in a year """

    low = balance / 12
    high = returnbalance(balance,0) / 12
    ans = (low + high ) / 2.0
    fixedsum = ans

    while returnbalance(balance,fixedsum) != 0:

        if returnbalance(balance,fixedsum)<0:
            high = ans
            ans = (low + high ) / 2.0
            fixedsum = ans
            returnbalance(balance,fixedsum)

            if round(returnbalance(balance,fixedsum),2) == -0.01: # Comparing with an epsilon
                final = round((fixedsum),2)
                break
            
        elif returnbalance(balance,fixedsum)>0:
            low = ans
            ans = (low + high ) / 2.0
            fixedsum = ans
            returnbalance(balance,fixedsum)

    print "Lowest Payment: " + str(final)


findfixedsumquick(balance,annualInterestRate)



# Finding Time
def call():
    """
    Function to measure the time taken.
    """
    findfixedsumquick(balance,annualInterestRate)



# This timer module requires a function    
t = Timer(call)
print "Time Bisection " + str(t.timeit(number=1))














    
