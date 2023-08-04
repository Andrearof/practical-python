# fileparse.py
#
# Exercise 3.3

# Exercise 3.4: Building a Column Selector
"""
 Modify the parse_csv() function so that it optionally allows user-specified columns to be picked out
"""

import csv


def parse_csv(filename, select=None):
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

            record = dict(zip(headers, row))
            records.append(record)

    return records


# portfolio = parse_csv("Work/Data/portfolio.csv")
# print(portfolio)

portfolio = parse_csv("Work/Data/portfolio.csv", select=["name", "price"])
print(portfolio)
