# Exercise 7.2: Passing tuple and dicts as arguments

from stock import Stock


data = ("GOOG", 100, 490.1)

s = Stock(*data)
print(s)

data2 = {"name": "GOOG", "shares": 100, "price": 490.1}
t = Stock(**data2)
print(t)
