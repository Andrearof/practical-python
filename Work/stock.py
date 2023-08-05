# Exercise 4.1: Objects as Data Structures

"""
Define a class Stock that represents a single holding of stock. Have the instances of Stock have name, shares, and price attributes.
"""


class Stock:
    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price


a = Stock("GOOG", 100, 490.10)
b = Stock("AAPL", 50, 122.34)
c = Stock("IBM", 75, 91.75)
print(b.shares * b.price)
print(c.shares * c.price)
stocks = [a, b, c]
for s in stocks:
    print(f"{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}")
