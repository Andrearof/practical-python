# Exercise 4.2: Adding some Methods

"""
 Add a cost() and sell() method to your Stock object.
"""


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


s = Stock("GOOG", 100, 490.10)
print(s.cost())
print(s.shares)
s.sell(25)
print(s.shares)
print(s.cost())
