from typing import List, Tuple


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        base_buy_index, base_sell_index, base_profit = find_profit(prices, 0, len(prices))

        # no way to gain any profit
        if base_profit == 0:
            return 0

        # look for profit on the left and right of the base transaction
        profit = max(find_profit(prices, 0, base_buy_index)[2] + base_profit,
                     find_profit(prices, base_sell_index + 1, len(prices))[2] + base_profit)

        # look for profit inside of base transactions on either buy or sell side
        buy_index1, sell_index1, profit1 = find_profit(prices, base_buy_index, base_sell_index - 1)
        buy_index2, sell_index2, profit2 = find_profit(prices, sell_index1 + 1, base_sell_index + 1)

        return max(profit, profit1 + profit2)

    def maxProfitBruteForce(self, prices: List[int]) -> int:
        """Brute force solution"""
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


def find_profit(prices: List[int], start: int, stop: int) -> Tuple[int, int, int]:
    if start >= len(prices):
        return 0, 0, 0
    buy_index = start
    sell_index = start
    curr_buy_index = start
    buy_price = prices[buy_index]
    max_profit = 0
    for i in range(start + 1, stop):
        profit = prices[i] - buy_price
        if profit > max_profit:
            sell_index = i
            buy_index = curr_buy_index
            max_profit = profit
        if prices[i] < buy_price:
            curr_buy_index = i
            buy_price = prices[i]
    return buy_index, sell_index, max_profit


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
