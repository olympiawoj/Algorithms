#!/usr/bin/python

import sys

# amount is in cents
# denominations is an array of coin demoninations
# returns total # of permutations of change for input using the coin denominations
# making_change(10) //4
# 1) what denominations are available? penny, nickel, dime, quarter, half dollar

"""
0 --> 0
1 --> 1
2 --> 1
3 --> 1
4 --> 1
5 --> 2 (5 pennies, 1 nickle)
6 --> 2 (6 pennies, 1 nickle 1 penny)
7
8
9
10 --> 4
11 --> 4(11 pennies, 6 pennies 1 nickle, 2 nickles 1 penny, 1 dime 1 penny)
12
13
14
15 --> 6 (
  15 pennies,
  10 pennies 1 nickle,
  5 pennies 2 nickles,
  3 nickles,
  1 dime 1 nickle
  1 dime 5 pennies
   )


Base case -
if amount is 0, then return
"""


def making_change(amount, denominations):

    # cache = [0] * (amount + 1)
    # creates a cache
    print('this is amount', amount)
    # initialize an array with 11 indices (0-10)
    cache = [0 for _ in range(amount + 1)]
    # Set the 0 indice to 1 bc there's only 1 combo of 0 coins and thats none
    cache[0] = 1
    print('this is the cache', cache)
    # for every denomination1, 5, 10, 25, 50
    for coinVal in denominations:
      # For every element in a range of 11
        for i in range(coinVal, amount + 1):
            print(f'i: {i}, coin:{coinVal}')
            # the total is the index minus the denomination

            total = i - coinVal
            print('this is the total', total)
            # cache at index is concatenated with cache[total]
            cache[i] += cache[total]
            print('this is the cache', cache)
    return cache[amount]


print(making_change(10, [1, 5, 10, 25, 50]))

# if __name__ == "__main__":
#     # Test our your implementation from the command line
#     # with `python making_change.py [amount]` with different amounts
#     if len(sys.argv) > 1:
#         denominations = [1, 5, 10, 25, 50]
#         amount = int(sys.argv[1])
#         print("There are {ways} ways to make {amount} cents.".format(
#             ways=making_change(amount, denominations), amount=amount))
#     else:
#         print("Usage: making_change.py [amount]")
