# Exercise 1.26

"""
Read the entire file as a big string
"""

# with open("Work/Data/portfolio.csv", "rt") as f:
#     data = f.read()

# print(data)

"""
Read file line by line
"""

# with open("Work/Data/portfolio.csv", "rt") as f:
#     for line in f:
#         print(line, end="")

"""
Manually skip some lines
"""

# f = open("Work/Data/portfolio.csv", "rt")
# headers = next(f)
# print(headers)
# for line in f:
#     print(line, end="")
# f.close()

"""
Split read lines
"""

f = open("Work/Data/portfolio.csv", "rt")
headers = next(f)
print(headers.split(","))
for line in f:
    row = line.split(",")
    print(row)
f.close()
