# Exercise 5.8: Adding slots

from fileparse import parse_csv


class Stock:
    __slots__ = ("name", "_shares", "price")

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self._shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f"({self.name}, {self.shares}, {self.price})"

    @property
    def shares(self) -> int:
        return self._shares

    @shares.setter
    def shares(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Expected int")
        self._shares = value

    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, stocks_number: int) -> None:
        self.shares -= stocks_number
        return
