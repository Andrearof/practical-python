# pcost.py
#
# Exercise 1.27

"""
The columns in portfolio.csv correspond to the stock name, number of shares, and purchase price of a single stock holding.
Write a program called pcost.py that opens this file, reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio.

Output = Total cost 44671.15
"""

# Exercise 1.30

"""
Turn pcost.py into a function that takes a filename and returns the total cost
"""

# Exercise 1.31

"""
Catch the exception
"""

# Exercise 2.15: A practical enumerate() example

"""
Recall that the file Data/missing.csv contains data for a stock portfolio, but has some rows with missing data. 
Using enumerate(), modify your pcost.py program so that it prints a line number with the warning message when it encounters bad input
"""


def portfolio_cost(filename):
    total_cost = 0
    with open(filename, "rt") as file:
        next(file)
        for number, line in enumerate(file, start=1):
            row = line.split(",")
            try:
                total_cost += float(row[1]) * float(row[2])
            except ValueError:
                print(f"Row {number}: Bad row: {row}")

    return total_cost


# cost = portfolio_cost("Work/Data/portfolio.csv")
# print(f"Total cost: {cost}")

cost = portfolio_cost("Work/Data/missing.csv")
print(cost)
