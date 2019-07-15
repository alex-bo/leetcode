from random import randint
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = [n for n in self.nums]
        for i in range(1, len(nums)):
            j = randint(0, i)
            nums[i], nums[j] = nums[j], nums[i]
        return nums


def test_one(nums: List[int]) -> bool:
    nums_copy = [n for n in nums]
    print(nums)
    solution = Solution(nums)
    shfl = solution.shuffle()
    print(shfl)
    rst = solution.reset()
    if rst == nums:
        print('OK')
        return True
    else:
        print('WRONG! Got {}, expected {}.'.format(rst, nums))
        return False


def test():
    test_one([1, 2, 3])


if __name__ == '__main__':
    test()
