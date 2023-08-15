# Exercise 7.5: Sorting on a field

from report import read_portfolio

portfolio = list(read_portfolio("Work/Data/portfolio.csv"))


def stock_name(s):
    return s.name


portfolio.sort(key=stock_name)
for s in portfolio:
    print(s)
