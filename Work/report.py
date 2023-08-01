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
pprint(portfolio)
print(f"Total cost: {total_cost}")
