# Exercise 7.1: A simple example of variable arguments


def avg(x, *more):
    return float(x + sum(more)) / (1 + len(more))


print(avg(1, 2, 3, 4, 5, 6))
