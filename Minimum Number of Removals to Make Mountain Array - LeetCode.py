from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        uphill_dp = calculate_uphill_counts(nums)
        downhill_dp = calculate_uphill_counts(nums[::-1])[::-1]
        max_cnt = 0
        for i in range(1, len(nums) - 1):
            if uphill_dp[i] > 1 and downhill_dp[i] > 1:
                max_cnt = max(max_cnt, uphill_dp[i] + downhill_dp[i] - 1)
        return len(nums) - max_cnt


def calculate_uphill_counts(nums: List[int]) -> List[int]:
    dp = [1 for _ in range(len(nums))]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


if __name__ == '__main__':
    print(2, Solution().minimumMountainRemovals([9, 8, 1, 7, 6, 5, 4, 3, 2, 1]))
    print(6, Solution().minimumMountainRemovals([100, 92, 89, 77, 74, 66, 64, 66, 64]))
