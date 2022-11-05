from bisect import bisect_left
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        results = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sm = nums[i] + nums[j] + nums[k]
                if sm == 0:
                    results.append([nums[i], nums[j], nums[k]])
                    prev = nums[k]
                    while nums[k] == prev and j < k:
                        k -= 1
                    prev = nums[j]
                    while nums[j] == prev and j < k:
                        j += 1
                elif sm > 0:
                    k -= 1
                else:
                    j += 1

        return results


if __name__ == '__main__':
    print('', [[-1, -1, 2], [-1, 0, 1]], '\n', Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print('', [[0, 0, 0]], '\n', Solution().threeSum([0, 0, 0, 0]))
    print('', [[0, 0, 0]], '\n', Solution().threeSum([0, 0, 0]))
    print('', [[-2, 0, 2], [-2, 1, 1]], '\n', Solution().threeSum([-2, 0, 1, 1, 2]))
    print('', [[0, 0, 0]], '\n', Solution().threeSum([0 for _ in range(3000)]))
