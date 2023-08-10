# Exercise 6.13: Generator Expressions


nums = [1, 2, 3, 4, 5]
squares = (x * x for x in nums)
print(squares)
for n in squares:
    print(n)
