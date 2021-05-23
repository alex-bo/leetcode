from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if not arr:
            return 0
        dp = [0 for _ in arr]
        for i, n in enumerate(arr):
            max_n = n
            for j in range(k):
                if j > i:
                    break
                max_n = max(max_n, arr[i - j])
                dp[i] = max(
                    dp[i],
                    max_n * (j + 1) + (0 if i == j else dp[i - j - 1])
                )
        return dp[-1]


if __name__ == '__main__':
    print(14, Solution().maxSumAfterPartitioning([3, 7], 2))
    print(84, Solution().maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))
    print(83, Solution().maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
