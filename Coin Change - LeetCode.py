from time import time
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = dict()
        coins = sorted(coins)[::-1]
        res = find_next(coins, amount, cache)
        return res


def find_next(coins: List[int], amount: int, cache: dict):
    solution = float('inf')
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if amount in cache:
        return cache[amount]
    for c in coins:
        res = find_next(coins, amount - c, cache)
        if -1 < res < solution:
            solution = res + 1
    cache[amount] = -1 if solution == float('inf') else solution
    return cache[amount]


def main():
    test([1, 2, 5], 11, 3)
    test([1, 2, 5], 0, 0)
    test([2], 3, -1)
    test([3, 4, 5, 6], 3, 1)
    test([3, 4, 5, 6], 6, 1)
    test([3, 4, 5, 6], 4, 1)
    test([3, 4, 5, 6], 20, 4)
    test([2, 3, 4, 5, 6], 19, 4)
    test([2, 3, 4, 5, 6], 10, 2)
    test([2, 3, 4, 5, 6], 100, 17)
    # test([2, 3, 4, 5, 6], 5969, 995)
    # test([186, 419, 83, 408], 6249, 26)
    test([186, 419, 83, 408], 6249, 20)


def test(coins: List[int], amount: int, expected_coins: int) -> None:
    start = time()
    error = False
    actual_coins = 0
    try:
        actual_coins = Solution().coinChange(coins, amount)
    except:
        error = True
        raise
    result = 'SUCCESS'
    if error:
        result = 'EXCEPTION'
    elif actual_coins != expected_coins:
        result = 'FAIL expected {} got {}'.format(expected_coins, actual_coins)
    print(('coinChange({coins}, {amount}) = {actual_coins}\t'
           '{time}s\t'
           '{result}').format(
        coins=coins,
        amount=amount,
        actual_coins=actual_coins,
        time=round(time() - start, 1),
        result=result
    ))


if __name__ == '__main__':
    main()


'''
#########################
# somebody's solution
#########################

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] * (amount + 1)
        MAX = float("inf")

        # Number of coins needed for coin amount is 1
        # Make sure to exclude sums larger than amount. No need of it
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, amount + 1):
            # Don't calculate if its a coin that already exists
            if i in coins: continue
            # 1 + min(dp[current value - current coin])
            # The 1 is because we are using current coin
            # dp[i] = 1 + min(dp[i - coin] if i - coin >= 0 else MAX for coin in coins)

            lst = []
            for coin in coins:
                if i - coin >= 0:
                    lst.append(dp[i - coin])
                else:
                    lst.append(MAX)
            dp[i] = 1 + min(lst)


        return -1 if dp[-1] == MAX else dp[-1]
'''

'''
#########################
# brute force solution from LeetCode
#########################

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return find_next(0, coins, amount)


def find_next(idx: int, coins: List[int], amount: int):
    if amount == 0:
        return 0
    if idx < len(coins) and amount > 0:
        max_val = int(amount / coins[idx])
        min_cost = float('inf')
        for x in range(0, max_val+1):
            if amount >= (x * coins[idx]):
                res = find_next(idx + 1, coins, amount - x*coins[idx])
                if res != -1:
                    min_cost = min(min_cost, res + x)
        if min_cost != float('inf'):
            return min_cost
    return -1
'''