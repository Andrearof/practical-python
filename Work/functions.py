# Exercise 1.29

"""
Define a function
"""


def greeting(name):
    "Issues a greeting"
    print(f"Hello {name}")


# greeting("Guido")
# greeting("Paula")

# Exercise 1.30

"""
Turn pcost.py into a function that takes a filename and returns the total cost
"""


def portfolio_cost(filename):
    total_cost = 0
    with open(filename, "rt") as file:
        next(file)
        for line in file:
            row = line.split(",")
            try:
                total_cost += float(row[1]) * float(row[2])
            except ValueError:
                print("Couldn't parse data, invalid format.")

    return total_cost


cost = portfolio_cost("Work/Data/portfolio.csv")
# print(f"Total cost: {cost}")

# Exercise 1.31

"""
Catch the exception
"""
portfolio_cost("Work/Data/missing.csv")
