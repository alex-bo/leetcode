from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return solution_1d_bottom_up(amount, coins)


def solution_1d_bottom_up(amount: int, coins: List[int]) -> int:
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1
    for i, coin in enumerate(sorted(coins)):
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]
    return dp[-1]


def solution_recursive(amount: int, coins: List[int], i: int, cache: dict) -> int:
    key = (amount, i)
    if key not in cache:
        if amount < 0:  # we missed the target
            cache[key] = 0
        elif amount == 0:  # reached target amount
            cache[key] = 1
        elif i == len(coins):  # out of coins
            cache[key] = 0
        else:
            cache[key] = (
                    solution_recursive(amount - coins[i], coins, i, cache)
                    + solution_recursive(amount, coins, i + 1, cache)
            )
    return cache[key]


if __name__ == '__main__':
    print(Solution().change(5, [1, 2, 5]))
    print(Solution().change(500, [1, 2, 5]))
