from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = Counter(nums)
        prev = 0
        include, exclude = 0, 0
        for n in sorted(counts):
            if n == (prev + 1):
                exclude, include = max(exclude, include), n * counts[n] + exclude
            else:
                exclude, include = max(exclude, include), n * counts[n] + max(exclude, include)
            prev = n
        return max(include, exclude)


if __name__ == '__main__':
    print(6, Solution().deleteAndEarn([3, 4, 2]))
    print(9, Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]))
    print(9, Solution().deleteAndEarn([3, 3, 3, 4, 2]))
