#!/usr/bin/python

"""
1) Understand -

Functions
- find_max_profit should receive a list of stock prices as an input, return the max profit that can be made from a single buy and sell. You must buy first before selling, no shorting

- prices is an array of integers which represent stock prices and we need to find the max, the min, and subtract

- TO solve this, we need to find out the max profit and minimum 

[1, 3, 2]

Max profit = 2
3-2 = 1

[4, 8, 1]
I have to buy 4
Sell 8
Max profit = 4

So we start with the maxProfit = arr[1] - arr[0]
We need to track the min price arr[0]




TO DO
- Iterate through array prices 
- For each current_price, if that price - min price > maxProfit, then define a new max
- For each current price, if that cur price is less than the min price, define a new min


- Update variables if we find a higher max profit and/or a new min price



"""

import argparse


def find_max_profit(prices):

    # Tracks min price and current max profit
    minPrice = prices[0]
    maxProfit = prices[1] - minPrice

    # could also do
    # for currentPrice in prices[1:]
    for i in range(1, len(prices)):

        # Temp variable to store position of minimum element
        print('loop', prices[i])
        print('i', i)
        maxProfit = max(prices[i] - minPrice, maxProfit)

        minPrice = min(prices[i], minPrice)
        print('min', minPrice)
        print('maxProfit', maxProfit)

    return maxProfit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))


# print(find_max_profit([1050, 270, 1540, 3800, 2]))
