from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)

        if nums_sum % 2 != 0:
            return False

        return bottom_up_solution(nums, nums_sum // 2)
        # return top_down_solution(nums, nums_sum // 2, {})


def top_down_solution(nums: List[int], target: int, cache: dict) -> bool:
    if target == 0:
        return True
    if target < 0:
        return False

    if target not in cache:
        for i, n in enumerate(nums):
            if top_down_solution(nums[:i] + nums[i + 1:], target - n, cache):
                return True
        cache[target] = False
    return cache[target]


def bottom_up_solution(nums: List[int], target: int) -> bool:
    dp = [
        [False for _ in range(target + 1)] for _ in range(len(nums))
    ]
    for i in range(len(dp)):
        dp[i][0] = True
    for t in range(1, target + 1):
        res = False
        for i, num in enumerate(nums):
            res = res or num == t or (dp[i - 1][t - num] if i > 0 and num <= t else False)
            dp[i][t] = res

    return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().canPartition(
        [1, 5, 11, 5]
    ))
    print(Solution().canPartition(
        [2, 2, 1, 1]
    ))
