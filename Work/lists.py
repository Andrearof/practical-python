# Exercise 1.20

symlist = ["HPQ", "AAPL", "AIG", "MSFT", "YHOO", "GOOG"]

"""
The for loop works by looping over data in a sequence such as a list. 
"""

for s in symlist:
    print("s=", s)

"""
Use the in or not in operator to check if 'AIG','AA', and 'CAT' are in the list of symbols
"""
print("AIG" in symlist)  # True
print("AA" in symlist)  # False
print("CAT" not in symlist)  # True
