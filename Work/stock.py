# Exercise 4.9: Better output for printing objects

"""
Modify the Stock object that you defined in stock.py so that the __repr__() method produces more useful output.
"""

from fileparse import parse_csv


class Stock:
    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f"({self.name}, {self.shares}, {self.price})"

    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, stocks_number: int) -> None:
        self.shares -= stocks_number
        return


with open("Work/Data/portfolio.csv") as lines:
    port_dicts = parse_csv(
        lines, select=["name", "shares", "price"], types=[str, int, float]
    )

goog = Stock("GOOG", 100, 490.1)
print(goog)
