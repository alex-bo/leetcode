from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp_lis = [1 for _ in nums]
        dp_num = [1 for _ in nums]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                new_lis = dp_lis[j] + 1
                if dp_lis[i] < new_lis:
                    dp_num[i] = dp_num[j]
                    dp_lis[i] = new_lis
                elif dp_lis[i] == new_lis:
                    dp_num[i] += dp_num[j]
        res = 0
        lis = max(dp_lis)
        for i in range(len(nums)):
            if dp_lis[i] == lis:
                res += dp_num[i]
        return res


if __name__ == '__main__':
    print(3, Solution().findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))
