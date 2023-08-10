# Exercise 6.1: Iteration Illustrated

a = [1, 9, 4, 25, 16]

f = open("Work/Data/portfolio.csv")
print(next(f))
print(next(f))

i = a.__iter__()
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
