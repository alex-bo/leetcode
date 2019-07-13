from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - buy_price)
            buy_price = min(buy_price, prices[i])
        return profit


def test_one(prices: List[int], expected: int) -> bool:
    print(prices)
    actual = Solution().maxProfit(prices)
    if actual == expected:
        print('OK')
        return True
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))
        return False


def test():
    test_one([7, 1, 5, 3, 6, 4], 5)
    test_one([7, 6, 4, 3, 1], 0)


if __name__ == '__main__':
    test()
