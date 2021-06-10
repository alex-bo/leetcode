from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = [[nums[0]]]
        for i in range(1, len(nums)):
            res = permute(nums[i], res)
        return res


def permute(n: int, res: List[List[int]]) -> List[List[int]]:
    new_res = []
    for i in range(len(res[0]) + 1):
        for arr in res:
            new_res.append(arr[:i] + [n] + arr[i:])
    return new_res


if __name__ == '__main__':
    print(len(Solution().permute([1, 2, 3, 4])))
