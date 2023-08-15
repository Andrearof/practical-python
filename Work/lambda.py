# Exercise 7.6: Sorting on a field with lambda

from report import read_portfolio

portfolio = list(read_portfolio("Work/Data/portfolio.csv"))


def stock_name(s):
    return s.name


portfolio.sort(key=lambda s: s.price)

for s in portfolio:
    print(s)
