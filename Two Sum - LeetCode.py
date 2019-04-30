from time import time
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Brute force
        # time: O(N^2)
        # space: O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]

        # optimized
        # time: O(N)
        # space: O(N)
        cache = dict()
        for i, n in enumerate(nums):
            cache[n] = i

        for i, n1 in enumerate(nums):
            n2 = target - n1
            if n2 not in cache:
                continue
            if i == cache[n2]:
                continue
            return [i, cache[n2]]
        raise Exception('No solution!')


def main():
    test([0, 1], [2, 7, 11, 15], 9)
    test([1, 2], [3, 2, 4], 6)
    test([0, 1], [3, 3], 6)


def test(expected, *args) -> None:
    start = time()
    error = False
    actual = 0
    try:
        actual = Solution().twoSum(*args)
    except:
        error = True
        raise
    result = 'SUCCESS'
    if error:
        result = 'EXCEPTION'
    elif actual != expected:
        result = 'FAIL expected {} got {}'.format(expected, actual)
    print(('twoSum({args}) = {actual}\t'
           '{time}s\t'
           '{result}').format(
        args=args,
        actual=actual,
        time=round(time() - start, 1),
        result=result
    ))


if __name__ == '__main__':
    main()
