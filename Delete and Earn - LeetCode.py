from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = {}
        for n in range(min(nums), max(nums) + 1):
            for n in range(nums):
                dp[i] = max(
                    dp[i],
                    dp[j] + (0 if nums[i] in (nums[j] - 1, nums[j] + 1) else nums[i])
                )
        return dp[-1]


if __name__ == '__main__':
    # print(6, Solution().deleteAndEarn([3, 4, 2]))
    print(9, Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]))
    # TODO: finished here
    # print(9, Solution().deleteAndEarn([3, 3, 3, 4, 2]))
