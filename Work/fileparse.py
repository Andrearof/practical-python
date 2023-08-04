# fileparse.py
#
# Exercise 3.3

# Exercise 3.4: Building a Column Selector
"""
 Modify the parse_csv() function so that it optionally allows user-specified columns to be picked out
"""

# Exercise 3.5: Performing Type Conversion
"""
Modify the parse_csv() function so that it optionally allows type-conversions to be applied to the returned data
"""

# Exercise 3.6: Working without Headers

import csv


def parse_csv(filename, select=None, types=None, has_headers=False):
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as file:
        rows = csv.reader(file)

        # Headers
        headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:  # skip with no data
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row)]

            if has_headers:
                record = dict(zip(headers, row))
                records.append(record)
            else:
                record = tuple(row)
                records.append(record)

    return records


# portfolio = parse_csv("Work/Data/portfolio.csv")
# print(portfolio)

# portfolio = parse_csv(
#     "Work/Data/portfolio.csv", select=["name", "shares"], types=[str, float]
# )
# print(portfolio)

portfolio = parse_csv("Work/Data/prices.csv", types=[str, float], has_headers=False)
print(portfolio)
