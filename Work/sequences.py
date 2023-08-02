# Exercise 2.13: Counting

"""
Basic counting examples
"""

for n in range(10):
    # print(n, end=" ")  # 0 ... 9
    continue
for n in range(10, 0, -1):
    # print(n, end=" ")  # 10 ... 1
    continue
for n in range(0, 10, 2):
    # print(n, end=" ")  # 0, 2, ..., 8
    continue

# Exercise 2.14: More sequence operations

"""
Experiment with some of the sequence reduction operations
"""

data = [4, 9, 1, 25, 16, 100, 49]
# print(f"Min: {min(data)}")
# print(f"Max: {max(data)}")
# print(f"Sum: {sum(data)}")

for i, x in enumerate(data):
    print(i, x)
