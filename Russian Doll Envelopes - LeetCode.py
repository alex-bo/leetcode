from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda i: (i[0], -i[1]))
        return patience_sort_solution(envelopes)
        # return bottom_up_solution(envelopes)
        # return maxEnvelopes(envelopes)


def bottom_up_solution(envelopes: List[List[int]]) -> int:
    dp = [1 for _ in envelopes]
    res = 1
    for i in range(1, len(dp)):
        for j in range(i):
            if dp[j] + 1 > dp[i] and can_fit(envelopes[i], envelopes[j]):
                dp[i] = dp[j] + 1
                res = max(res, dp[i])
    return res


def can_fit(parent: List[int], child: List[int]) -> bool:
    return child[0] < parent[0] and child[1] < parent[1]


def patience_sort_solution(envelopes: List[List[int]]) -> int:
    nums = [n for _, n in envelopes]
    piles = []
    for n in nums:
        add_num(n, piles)
    return len(piles)


def add_num(num: int, piles: List[int]):
    lo, hi = 0, len(piles)
    while lo < hi:
        mid = (hi + lo) // 2
        if num <= piles[mid]:
            hi = mid
        else:
            lo = mid + 1
    if lo == len(piles):
        piles.append(num)
    else:
        piles[lo] = num


if __name__ == '__main__':
    print(3, Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))
    print(1, Solution().maxEnvelopes([[1, 1], [1, 1], [1, 1]]))
    print(5, Solution().maxEnvelopes(
        [[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380],[7, 980]]))
    print(1000, Solution().maxEnvelopes(list(zip(range(1000), range(1000)))))
