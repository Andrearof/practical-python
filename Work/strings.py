# Exercise 1.14

"""
Concatenates a new symbol “GOOG” to the end of symbols
so that the symbols variable holds the value 'AAPL,IBM,MSFT,YHOO,SCO,GOOG'
"""

symbols = "AAPL,IBM,MSFT,YHOO,SCO"

symbols = symbols + ",GOOG"

# print(symbols)

# Exercise 1.15

"""
Experiment with the in operator to check for substrings.
"""
# print("IBM" in symbols)
# print("AA" in symbols)  # True because 'AA' is present in symbols inside 'AAPL'
# print("CAT" in symbols)

# Exercise 1.16

"""
Try experimenting with some of the string methods.
"""

print(symbols.lower())
print(symbols.find("MSFT"))
print(symbols[13:17])
print(symbols.replace("SCO", "DOA"))
name = "    IBM     \n"
print(name.strip())
