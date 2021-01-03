from typing import List


def bottom_up_solution(nums: List[int]) -> int:
    dp = [1 for _ in nums]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] <= nums[i] and nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == '__main__':
    input()
    input_nums = [int(s) for s in input().split(' ')]
    print(bottom_up_solution(input_nums))
