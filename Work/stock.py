# Exercise 4.3: Creating a list of instances

"""
Make a list of Stock instances from a list of dictionaries. 
Then compute the total cost.
"""

from fileparse import parse_csv


class Stock:
    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, stocks_number: int) -> None:
        self.shares -= stocks_number
        return


with open("Work/Data/portfolio.csv") as lines:
    port_dicts = parse_csv(
        lines, select=["name", "shares", "price"], types=[str, int, float]
    )

portfolio = [Stock(d["name"], d["shares"], d["price"]) for d in port_dicts]
print(sum([s.cost() for s in portfolio]))
