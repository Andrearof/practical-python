# Exercise 2.1

"""
Create a tuple that represents the first row.
Use it to calculate total cost.
"""

import csv

file = open("Work/Data/portfolio.csv")
rows = csv.reader(file)
next(rows)
row = next(rows)
t = row[0], int(row[1]), float(row[2])
name, share, price = t
total_cost = share * price
# print(f"Total cost: {total_cost}")

# Exercise 2.2: Dictionaries as a data structure

"""
Create a dictionary instead and calculate the cost.
"""

d = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
# print(f"Total cost: {d['shares'] * d['price']}")

# Exercise 2.3: Some additional dictionary operations

# print(list(d))

# for key in d:
#     print(key, " = ", d[key])

# keys = d.keys()
# print(keys)
# del d["name"]
# print(keys)

items = d.items()

d2 = dict(items)
print(d2)
