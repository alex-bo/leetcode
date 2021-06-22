from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        start, end = swap_outlier(nums)
        in_place_reverse(nums, start, end)


def swap_outlier(nums: list) -> tuple:
    outlier = 0
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            outlier = i
            break
    else:
        return 0, len(nums) - 1

    for i in range(len(nums) - 1, outlier, -1):
        if nums[i] > nums[outlier]:
            nums[i], nums[outlier] = nums[outlier], nums[i]
            return outlier + 1, len(nums) - 1

    return 0, len(nums) - 1


def in_place_reverse(nums: list, start: int, end: int) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
