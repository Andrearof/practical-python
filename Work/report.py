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
        headers = next(rows)
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
    current_portfolio_value += prices.get(holding["name"], 0.0) * holding["shares"]

print(f"Total cost of portfolio: {total_cost}")
print(f"Current value of portfolio: {current_portfolio_value}")
print(f"Total gain/loss: {current_portfolio_value - total_cost}")
