from typing import List

# [max1, max2, n   , n+1, n+2, ...]
# [...., max1, max2, n, n+1, n+2, ...]


class Solution:
    def rob(self, nums: List[int]) -> int:
        max1, max2 = 0, 0
        for n in nums:
            max1, max2 = max2, max(max1 + n, max2)
        return max2


def test(nums: List[int], expected: int):
    print(nums)
    actual = Solution().rob(nums)
    if actual == expected:
        print('OK!')
    else:
        print('WRONG! Expected {}, got {}.'.format(expected, actual))


if __name__ == '__main__':
    test([1, 2, 3, 1], 4)
    test([2, 7, 9, 3, 1], 12)
    test([2, 1, 1, 2], 4)
