# mortgage.py
#
# Exercise 1.10
"""
Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation.
The interest rate is 5% and the monthly payment is $2684.11.
Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage:

1.8:
Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage.
Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.

1.9:
Modify the program so that extra payment information can be more generally handled
Make the program look at these variables and calculate the total paid appropriately.
How much will Dave pay if he pays an extra $1000/month for 4 years starting after the first five years have already been paid

1.10:
Modify the program to print out a table showing the month, total paid so far, and the remaining principal.
"""

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = int(
    input("Enter number of the month of the first extra payment: ")
)
extra_payment_end_month = int(
    input("Enter number of the month of the last extra payment: ")
)
extra_payment = int(input("Enter the value of the extra payment: "))
monthly_payment = 0

print("Month | Paid so far | Remaining principal")

while principal > 0:
    if extra_payment_start_month <= months <= extra_payment_end_month:
        monthly_payment = payment + extra_payment
    else:
        monthly_payment = payment
    principal = principal * (1 + rate / 12) - monthly_payment
    total_paid = total_paid + monthly_payment
    months += 1
    print(f"{months}    {total_paid}    {principal}")

print("Total paid: ", total_paid)
print("Number of months required: ", months)
