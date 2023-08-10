# Exercise 6.12: Putting it all together

from follow import follow
import csv
from report import read_portfolio
from tableformat import create_formatter


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def filter_symbols(rows, names):
    for row in rows:
        if row["name"] in names:
            yield row


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    return rows


def ticker(portfolio_file, log_file, format):
    portfolio = read_portfolio(portfolio_file)
    lines = follow(log_file)
    rows = parse_stock_data(lines)
    formatter = create_formatter(format)

    formatter.headings(["Name", "Price", "Change"])
    for name, price, change in rows:
        rowdata = [name, f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


if __name__ == "__main__":
    import sys

    ticker(sys.argv[1], sys.argv[2], sys.argv[3])
