import random
from typing import List

VISITED = -1


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or min((n for n in nums if n > 0), default=2) > 1:
            return 1

        max_num = max(nums)

        # reduce indexes by 1 and reassign if VISITED flag already in use by some cell
        for i in range(len(nums)):
            if nums[i] >= 0:
                nums[i] -= 1
            if nums[i] == VISITED:
                nums[i] = -2

        # visit all cells by value of ith element
        i = 0
        while i < len(nums):
            if 0 <= nums[i] < len(nums) and nums[nums[i]] != VISITED:
                if i == nums[i]:
                    nums[i] = VISITED
                    i += 1
                else:
                    nums[nums[i]], nums[i] = VISITED, nums[nums[i]]
            else:
                i += 1

        # first not visited cell is what we're looking for...
        for i in range(len(nums)):
            if nums[i] != VISITED:
                return i + 1

        return max_num + 1


def test_one(nums: List[int], expected: int):
    print(nums)
    actual = Solution().firstMissingPositive(nums)
    if expected == actual:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}!'.format(actual, expected))


if __name__ == '__main__':
    test_one([1, 3, 3], 2)
    test_one([1, 1000], 2)
    test_one([-5], 1)
    test_one([], 1)
    test_one([-1, -2, -3], 1)
    test_one([1, 2, 0], 3)
    test_one([3, 4, -1, 1], 2)
    test_one([7, 8, 9, 11, 12], 1)
    lst = list(range(30))
    r = random.randint(1, len(lst) - 1)
    lst.remove(r)
    random.shuffle(lst)
    test_one(lst, r)
