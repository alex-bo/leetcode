#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getNumberOfOptions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY priceOfJeans
#  2. INTEGER_ARRAY priceOfShoes
#  3. INTEGER_ARRAY priceOfSkirts
#  4. INTEGER_ARRAY priceOfTops
#  5. INTEGER dollars
#
from time import time

from typing import List


def getNumberOfOptionsBottomUp(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars):
    return bottom_up_solution(
        [
            priceOfJeans,
            priceOfShoes,
            priceOfSkirts,
            priceOfTops
        ],
        dollars
    )


def getNumberOfOptionsTopDown(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars):
    return top_down_recursive_solution(
        [
            priceOfJeans,
            priceOfShoes,
            priceOfSkirts,
            priceOfTops
        ],
        0,
        dollars,
        {}
    )


def bottom_up_solution(list_of_prices: List[List[int]], dollars: int) -> int:
    dp = [
        [0 for _ in range(dollars + 1)] for _ in list_of_prices
    ]
    # print_grid(dp)
    for i, prices in enumerate(list_of_prices):
        for price in prices:
            if i == 0:
                for amt in range(price, dollars + 1):
                    dp[i][amt] += 1
                    # print_grid(dp)
            else:
                for amt in range(price + 1, dollars + 1):
                    dp[i][amt] += dp[i - 1][amt - price]
                    # print_grid(dp)
    return dp[-1][-1]


def print_grid(grid: List[List[int]]):
    print('-' * len(grid))
    for r in grid:
        print(r)


def top_down_recursive_solution(prices: List[List[int]], prices_index: int, dollars: int, cache: dict) -> int:
    if prices_index >= len(prices):
        if dollars >= 0:
            return 1
        return 0
    if prices_index not in cache:
        cache[prices_index] = {}
    if dollars not in cache[prices_index]:
        res = 0
        for price in prices[prices_index]:
            if dollars >= price:
                res += top_down_recursive_solution(prices, prices_index + 1, dollars - price, cache)
        cache[prices_index][dollars] = res
    return cache[prices_index][dollars]


def test_all(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars):
    start = time()
    print(
        'getNumberOfOptionsTopDown\t\t\t',
        getNumberOfOptionsTopDown(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars),
        round(time() - start, 2),
        'seconds'
    )
    start = time()
    print(
        'getNumberOfOptionsBottomUp\t\t\t',
        getNumberOfOptionsBottomUp(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars),
        round(time() - start, 2),
        'seconds'
    )


if __name__ == '__main__':
    '''
    number of items in array <= 10^6
    max price (and amount) <= 10^9
    '''
    # test_all(
    #     [2, 3],
    #     [4],
    #     [2, 3],
    #     [1, 2],
    #     10000000
    # )
    test_all(
        list(range(1, 10000)),
        list(range(1, 10000)),
        list(range(1, 100)),
        list(range(1, 100)),
        10000
    )
