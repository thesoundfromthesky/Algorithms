#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_min_price_so_far = 0
    max_profit_so_far = None

    for i in range(0, len(prices)-1):
        if prices[i] > prices[i+1]:
            current_min_price_so_far = i + 1
        else:
            break

    for i in range(current_min_price_so_far, len(prices) - 1):
        if prices[i] < prices[i+1]:
            max_profit_so_far = i + 1
        else:
            break

    if max_profit_so_far is None:
        return 0 - prices[current_min_price_so_far]
    else:
        return prices[max_profit_so_far] - prices[current_min_price_so_far]


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
