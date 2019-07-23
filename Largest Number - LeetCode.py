import functools
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """DFS"""

        def compare(left: str, right: str) -> int:
            return int(left + right) - int(right + left)

        return (''.join(sorted((str(n) for n in nums),
                               key=functools.cmp_to_key(compare),
                               reverse=True)).lstrip('0')
                or '0')


def test_one(nums: List[int], expected: str) -> bool:
    print(nums)
    actual = Solution().largestNumber(nums)
    if actual != expected:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))
        return False
    print('OK')
    return True


def test():
    test_one([10, 2], '210')
    test_one([3, 30, 34, 5, 9], '9534330')
    test_one([1, 1, 1], '111')
    test_one([121, 12], '12121')
    test_one([0, 0, 0, 0], '0')


if __name__ == '__main__':
    test()
