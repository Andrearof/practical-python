# Exercise 5.6: Simple Properties

from fileparse import parse_csv


class Stock:
    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f"({self.name}, {self.shares}, {self.price})"

    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, stocks_number: int) -> None:
        self.shares -= stocks_number
        return


goog = Stock("GOOG", 100, 490.1)
print(goog.cost)
