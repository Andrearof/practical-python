# Exercise 6.4: A Simple Generator


def filematch(filename, substr):
    with open(filename, "r") as file:
        for line in file:
            if substr in line:
                yield line


for line in filematch("Work/Data/portfolio.csv", "IBM"):
    print(line, end="")
