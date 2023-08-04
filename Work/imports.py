# Exercise 3.11: Module imports

# import bounce
# import mortgage
# import report
import fileparse

portfolio = fileparse.parse_csv(
    "Work/Data/portfolio.csv",
    select=["name", "shares", "price"],
    types=[str, int, float],
)
