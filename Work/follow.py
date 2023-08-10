# Exercise 6.7: Watching your portfolio

import os
import time


def follow(filename):
    file = open(filename)
    file.seek(0, os.SEEK_END)

    while True:
        line = file.readline()
        if line == "":
            time.sleep(0.1)
            continue
        yield line


if __name__ == "__main__":
    from report import read_portfolio

    portfolio = read_portfolio("Work/Data/portfolio.csv")

    for line in follow("Work/Data/stocklog.csv"):
        fields = line.split(",")
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f"{name:>10s} {price:>10.2f} {change:>10.2f}")
