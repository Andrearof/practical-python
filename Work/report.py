# report.py

# Exercise 4.4: Using your class

"""
Modify the read_portfolio() function in the report.py program so that it reads a portfolio into a list of Stock instances
"""

import fileparse
from stock import Stock
from tableformat import TableFormatter


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    """
    with open(filename) as lines:
        port_dicts = fileparse.parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float]
        )
        port_objs = [Stock(d["name"], d["shares"], d["price"]) for d in port_dicts]
        return port_objs


def read_prices(filename):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def make_report_data(portfolio, prices):
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    rows = []
    for stock in portfolio:
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        rows.append(summary)
    return rows


def print_report(reportdata, formatter: TableFormatter):
    """
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    # print("%10s %10s %10s %10s" % headers)
    # print(("-" * 10 + " ") * len(headers))
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile):
    """
    Make a stock report given portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = TableFormatter()
    print_report(report, formatter)


def main(args):
    if len(args) != 3:
        raise SystemExit("Usage: %s portfile pricefile" % args[0])
    portfolio_report(args[1], args[2])


if __name__ == "__main__":
    import sys

    main(sys.argv)
