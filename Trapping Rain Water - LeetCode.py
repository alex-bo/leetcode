from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        return dynamic_programming(height)


def brute_force(height: List[int]) -> int:
    res = 0
    for i, h in enumerate(height[1:len(height)-1]):
        i += 1
        left_max = max(height[0:i])
        right_max = max(height[i+1:])
        res += max(0, min(left_max, right_max) - h)
    return res


def dynamic_programming(height: List[int]) -> int:
    left_min = [0 for _ in height]
    right_min = [0 for _ in height]
    for i in range(len(height)):
        left_min[i] = max(
            height[i],
            left_min[i - 1] if i > 0 else 0
        )
    for i in range(len(height) - 1, -1, -1):
        right_min[i] = max(
            height[i],
            right_min[i + 1] if i < (len(height) - 1) else 0
        )
    res = 0
    for left, right, h in zip(left_min, right_min, height):
        res += max(0, min(left, right) - h)
    return res


def test_one(height: List[int], expected: int):
    print(height)
    actual = Solution().trap(height)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}!'.format(actual, expected))


if __name__ == '__main__':
    test_one([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)

