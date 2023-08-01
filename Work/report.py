# report.py
#
# Exercise 2.5: List of Dictionaries

"""
Define a function read_portfolio(filename) that opens a given portfolio file and reads it into a dictionary
"""

import csv
from pprint import pprint


def read_portfolio(filename):
    """Computes the total cost (shares*price) of a portfolio file"""
    portfolio = []
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(holding)
            total_cost += holding["shares"] * holding["price"]
    return portfolio, total_cost


portfolio, total_cost = read_portfolio("Work/Data/portfolio.csv")
# pprint(portfolio)
# print(f"Total cost: {total_cost}")

# Exercise 2.6: Dictionaries as a container

"""
Write a function read_prices(filename) that reads a set of prices into a dictionary where the keys of the dictionary are the stock names and the values in the dictionary are the stock prices.
"""


def read_prices(filename):
    prices = {}

    with open(filename, "rt") as file:
        rows = csv.reader(file)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])
    return prices


prices = read_prices("Work/Data/prices.csv")
# pprint(prices)

# Exercise 2.7: Finding out if you can retire

"""
Tie all of this work together by adding a few additional statements to your report.py program that computes gain/loss. These statements should take the list of stocks in Exercise 2.5 and the dictionary of prices in Exercise 2.6 and compute the current value of the portfolio along with the gain/loss.
"""

current_portfolio_value = 0.0
for holding in portfolio:
    current_portfolio_value += prices.get(holding["name"]) * holding["shares"]

# print(f"Total cost of portfolio: {total_cost}")
# print(f"Current value of portfolio: {current_portfolio_value}")
# print(f"Total gain/loss: {current_portfolio_value - total_cost}")

# Exercise 2.9: Collecting Data

"""
Write a function make_report() that takes a list of stocks and dictionary of prices as input and returns a list of tuples containing the rows of the above table
"""


def make_report(portfolio, prices):
    report = []
    for holding in portfolio:
        r = (
            holding["name"],
            holding["shares"],
            prices[holding["name"]],
            prices[holding["name"]] - holding["price"],
        )
        report.append(r)
    return report


report = make_report(portfolio, prices)
# for r in report:
#     print(r)

# Exercise 2.10: Printing a formatted table

"""
Redo the for-loop in Exercise 2.9, but change the print statement to format the tuples
"""

# for name, shares, price, change in report:
#     print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")

# Exercise 2.11: Adding some headers

"""
Add header and separators
"""

headers = ("Name", "Shares", "Price", "Change")

name, shares, price, change = headers
# print(f"{name:>10s} {shares:>10s} {price:>10s} {change:>10s}")
# print(f"{'':-<10s} {'':->10s} {'':->10s} {'':->10s}")
# for name, shares, price, change in report:
#     print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")

# Exercise 2.11: Adding some headers
"""
How would you modify your code so that the price includes the currency symbol ($) ?
"""

print(f"{name:>10s} {shares:>10s} {price:>10s} {change:>10s}")
print(f"{'':-<10s} {'':->10s} {'':->10s} {'':->10s}")
for name, shares, price, change in report:
    price = str(round(price, 2))
    print(f"{name:>10s} {shares:>10d} {'$' + price:>10s} {change:>10.2f}")
