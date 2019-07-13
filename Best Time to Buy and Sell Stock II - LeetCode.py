from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy_profit = -prices[0]
        sell_profit = 0
        for i in range(1, len(prices)):
            sell_profit = max(sell_profit, buy_profit + prices[i])
            buy_profit = max(buy_profit, sell_profit - prices[i])
        return sell_profit


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
    test_one([7, 1, 5, 3, 6, 4], 7)
    test_one([1, 2, 3, 4, 5], 4)
    test_one([7, 6, 4, 3, 1], 0)


if __name__ == '__main__':
    test()
