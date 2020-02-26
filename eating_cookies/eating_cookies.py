#!/usr/bin/python
"""
1. Understand

We're finding all permutations of ways he could eat - this potentially means use recursion

Base case- if we have 0 more cookies to eat or negative cookies, return


Write out the permutations for small values of n by hand and see if you can find a pattern to calculate the total for any n. Once you find the pattern, it becomes a lot easier to plan out what you're going to code.


Combinations are arrangements of objects without regard for order, selected from a number of objects
Permutations are the number of possible arrangements in an ordered set of objects
If the order doesn't matter, it's a combination. If it does matter, it's a permutation. 


"""
import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

"""
# 0 -> 1
# 1 -> 1
# 2 -> 2
# 3 -> 4
# 4 -> 7
# 5 -> 13
# 10 -> 274

- Might have recognized the pattern and say this is Tribinocci


A recursive function that calls itself more than 1 time is exponential - it's going to break down.

This is no cache with fib - we can fix this easily and quickly

TypeError: 'NoneType' object does not support item assignment --> cache is None by defalut instead of a dictionary. TO FIX THIS, we need to instantiate the cache

. Don't ever declare things inside of a function definition bc weird things happen. Python happens that as it gets instantiated at compile, not at call. so you'll have 1 in global scope that'll get reused and if you call function a second time, what will still be there is all data from first time

"""


def eating_cookies(n, cache=None):

    # Base case
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # elif n == 1:
    #     return 1
    # Adds cache
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        # if not cache:
        #     # cache is not a list, it's key value pairs, so put base caches in cache
        #     # This i:0 for i in range is a *dictionary comprehension* - using a function to fill up a dictionary with zeros, that way our elif cache and cache[n]>0 will work
        #     # If cache was cache={} it won't be used bc its being instantiated every single time
        #     cache = {i: 0 for i in range(n+1)}
        #     print(cache)
        if cache is None:
            cache = {}

        value = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

        cache[n] = value

        return value


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
