# report.py
#
# Exercise 2.5: List of Dictionaries

"""
Define a function read_portfolio(filename) that opens a given portfolio file and reads it into a dictionary
"""

import csv
from pprint import pprint
from collections import Counter


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


# portfolio, total_cost = read_portfolio("Work/Data/portfolio.csv")
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


# prices = read_prices("Work/Data/prices.csv")
# pprint(prices)

# Exercise 2.7: Finding out if you can retire

"""
Tie all of this work together by adding a few additional statements to your report.py program that computes gain/loss. These statements should take the list of stocks in Exercise 2.5 and the dictionary of prices in Exercise 2.6 and compute the current value of the portfolio along with the gain/loss.
"""

# current_portfolio_value = 0.0
# for holding in portfolio:
#     current_portfolio_value += prices.get(holding["name"]) * holding["shares"]

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


# report = make_report(portfolio, prices)
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

# print(f"{name:>10s} {shares:>10s} {price:>10s} {change:>10s}")
# print(f"{'':-<10s} {'':->10s} {'':->10s} {'':->10s}")
# for name, shares, price, change in report:
#     price = str(round(price, 2))
#     print(f"{name:>10s} {shares:>10d} {'$' + price:>10s} {change:>10.2f}")


# Exercise 2.18: Tabulating with Counters

"""
Use a Counter to tabulate the total number of shares of each stock
"""

portfolio, total_cost = read_portfolio("Work/Data/portfolio.csv")
holdings = Counter()
for s in portfolio:
    holdings[s["name"]] += s["shares"]
# print(holdings.most_common(3))

portfolio2, total_cost2 = read_portfolio("Work/Data/portfolio2.csv")
holdings2 = Counter()
for s in portfolio2:
    holdings2[s["name"]] += s["shares"]
# print(holdings2)

combined = holdings + holdings2
# print(combined)

# Exercise 2.19: List comprehensions

nums = [1, 2, 3, 4]
squares = [x * x for x in nums]
# print(squares)
twice = [2 * x for x in nums if x > 2]
# print(twice)

# Exercise 2.20: Sequence Reductions

"""
Compute the total cost of the portfolio using a single Python statement.
After you have done that, show how you can compute the current value of the portfolio using a single statement.
"""

portfolio3, _ = read_portfolio("Work/Data/portfolio.csv")
cost = sum([s["shares"] * s["price"] for s in portfolio3])
# print(cost)
prices = read_prices("Work/Data/prices.csv")
value = sum([s["shares"] * prices[s["name"]] for s in portfolio3])
# print(value)

# Exercise 2.21: Data Queries

"""
Try the following examples of various data queries:
First, a list of all portfolio holdings with more than 100 shares.
All portfolio holdings for MSFT and IBM stocks.
A list of all portfolio holdings that cost more than $10000.
"""
more100 = [s for s in portfolio3 if s["shares"] > 100]
# print(more100)
msftibm = [s for s in portfolio3 if s["name"] in {"MSFT", "IBM"}]
# print(msftibm)
cost10k = [s for s in portfolio3 if s["shares"] * s["price"] > 10000]
# print(cost10k)

# Exercise 2.22: Data Extraction

"""
Show how you could build a list of tuples (name, shares) where name and shares are taken from portfolio
"""

name_shares = [(s["name"], s["shares"]) for s in portfolio3]
# print(name_shares)

"""
Determine the set of unique stock names that appear in portfolio
"""

# Set comprehension
names = {s["name"] for s in portfolio3}
# print(names)

"""
Make a dictionary that maps the name of a stock to the total number of shares held
"""

holdings3 = {name: 0 for name in names}
for s in portfolio3:
    holdings3[s["name"]] += s["shares"]
print(holdings3)
