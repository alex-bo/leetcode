from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs:
            return 0
        return bottom_up_solution(pairs)


def bottom_up_solution(pairs: List[List[int]]) -> int:
    pairs.sort()
    dp = [1 for _ in pairs]
    for i in range(1, len(pairs)):
        for j in range(i):
            if can_chain(pairs[j], pairs[i]):
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def can_chain(parent: List[int], child: List[int]) -> bool:
    return parent[1] < child[0]


def greedy_solution(pairs: List[List[int]]) -> int:
    pairs.sort(key=lambda i: (i[1], i[0]))
    cur, res = -2 ** 32, 0
    for x, y in pairs:
        if x > cur:
            res += 1
            cur = y
    return res


if __name__ == '__main__':
    print(2, Solution().findLongestChain([[1, 2], [2, 3], [3, 4]]))
    print(3, Solution().findLongestChain([[-6, 9], [1, 6], [8, 10], [-1, 4], [-6, -2], [-9, 8], [-5, 3], [0, 3]]))
