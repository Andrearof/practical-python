# Exercise 7.7: Using Closures to Avoid Repetition

from typedproperty import typedproperty


class Stock:
    name = typedproperty("name", str)
    shares = typedproperty("shares", int)
    price = typedproperty("price", float)

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self._shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f"({self.name}, {self.shares}, {self.price})"

    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, stocks_number: int) -> None:
        self.shares -= stocks_number
        return
