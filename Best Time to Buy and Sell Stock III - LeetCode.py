from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """Brute force solution"""
        # TODO: optimize
        if not prices:
            return 0
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    continue
                profit1 = prices[j] - prices[i]
                profit2 = 0
                for k in range(j + 1, len(prices)):
                    for l in range(k + 1, len(prices)):
                        profit2 = max(
                            profit2,
                            prices[l] - prices[k]
                        )
                max_profit = max(max_profit, profit1 + profit2)
        return max_profit


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
    test_one([3, 3, 5, 0, 0, 3, 1, 4], 6)
    test_one([1, 2, 3, 4, 5], 4)
    test_one([7, 6, 4, 3, 1], 0)


if __name__ == '__main__':
    test()
