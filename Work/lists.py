# Exercise 1.20

symlist = ["HPQ", "AAPL", "AIG", "MSFT", "YHOO", "GOOG"]

"""
The for loop works by looping over data in a sequence such as a list. 
"""

for s in symlist:
    pass
    # print("s=", s)

"""
Use the in or not in operator to check if 'AIG','AA', and 'CAT' are in the list of symbols
"""
# print("AIG" in symlist)  # True
# print("AA" in symlist)  # False
# print("CAT" not in symlist)  # True

# Exercise 1.22

"""
Use the append() method to add the symbol 'RHT' to end of symlist
"""
symlist.append("RHT")
# print(symlist) # ['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

"""
Use the insert() method to insert the symbol 'AA' as the second item in the list.
"""
symlist.insert(1, "AA")
# print(symlist) # ['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

"""
Use the remove() method to remove 'MSFT' from the list.
"""
symlist.remove("MSFT")
# print(symlist)  # ['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']

"""
Append a duplicate entry for 'YHOO' at the end of the list
"""
symlist.append("YHOO")
# print(symlist)  # ['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT', 'YHOO']

"""
Use the index() method to find the first position of 'YHOO' in the list.
"""
# print(symlist.index("YHOO"))  # 4

"""
Count how many times 'YHOO' is in the list:
"""
# print(symlist.count("YHOO"))  # 2

"""
Remove the first occurrence of 'YHOO'.
"""
symlist.remove("YHOO")
# print(symlist)  # ['HPQ', 'AA', 'AAPL', 'AIG', 'GOOG', 'RHT', 'YHOO']

# Exercise 1.23
"""
Sort the list
"""
symlist.sort()
# print(symlist) # ['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']

"""
Sort in reverse
"""
symlist.sort(reverse=True)
print(symlist)  # ['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
