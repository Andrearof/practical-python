# mortgage.py
#
# Exercise 1.8
"""
Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation.
The interest rate is 5% and the monthly payment is $2684.11.
Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage:

Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage.
Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.
"""

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra = 1000
monthly_payment = 0

while principal > 0:
    if months < 12:
        monthly_payment = payment + extra
    else:
        monthly_payment = payment
    principal = principal * (1 + rate / 12) - monthly_payment
    total_paid = total_paid + monthly_payment
    months += 1

print("Total paid: ", total_paid)
print("Number of months required: ", months)
