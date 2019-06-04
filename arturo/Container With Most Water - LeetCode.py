from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        max_volume = get_volume(height, left, right)
        while left < right:
            lvol = get_volume(height, left+1, right)
            rvol = get_volume(height, left, right-1)
            max_volume = max(lvol, rvol, max_volume)
            if lvol > rvol:
                left += 1
            elif lvol < rvol:
                right -= 1
            elif height[left+1] < height[right-1]:
                left += 1
            else:
                right -= 1
        return max_volume


def get_volume(height: List[int], left: int, right: int) -> int:
    return min(height[left], height[right]) * (right - left)


def test_one(height: List[int], expected: int):
    print(height)
    actual = Solution().maxArea(height)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


def test():
    test_one([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)
    test_one([], 0)
    test_one([1, 1, 1, 1], 3)
    test_one([1, 1, 1, 1, 1, 1], 5)
    test_one([2, 1, 1, 1, 1, 2], 10)
    test_one([3, 1, 1, 1, 3, 2], 12)
    test_one([1, 2, 4, 3], 4)
    test_one([1, 3, 2, 5, 25, 24, 5], 24)


if __name__ == '__main__':
    test()
