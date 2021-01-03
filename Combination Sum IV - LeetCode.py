from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # return solution_bottom_up(nums, target)
        return solution_top_down(nums, target, {})


def solution_bottom_up(nums: List[int], target: int) -> int:
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    for t in range(1, target + 1):
        for n in nums:
            if n > t:
                continue
            dp[t] += dp[t - n]
    return dp[-1]


def solution_top_down(nums: List[int], target: int, cache: dict) -> int:
    if target == 0:
        return 1
    if target < 0:
        return 0
    if target not in cache:
        cache[target] = sum(solution_top_down(nums, target - n, cache) for n in nums)
    return cache[target]


if __name__ == '__main__':
    pass

