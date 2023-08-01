# report.py
#
# Exercise 2.4 : A list of tuples

"""
Define a function read_portfolio(filename) that opens a given portfolio file and reads it into a list of tuples
"""

import csv


def read_portfolio(filename):
    """Computes the total cost (shares*price) of a portfolio file"""
    portfolio = []
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = row[0], int(row[1]), float(row[2])
            portfolio.append(holding)
            total_cost += holding[1] * holding[2]
    return portfolio, total_cost


portfolio, total_cost = read_portfolio("Work/Data/portfolio.csv")
print(f"Portfolio: {portfolio}")
print(f"Total cost: {total_cost}")
