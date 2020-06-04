from typing import List, Dict


class Solution:

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        return dp_2d_solution(nums, S)


def bfs_solution(nums: List[int], S: int) -> int:
    q1, q2 = [0], []

    for n1 in nums:
        while q1:
            n2 = q1.pop()
            q2.append(n2 - n1)
            q2.append(n1 + n2)
        q1, q2 = q2, q1

    return len([i for i in q1 if i == S])


def dfs_with_memo_solution(nums: List[int], S: int) -> int:
    cache = [{} for _ in nums]
    return dfs(nums, 0, 0, S, cache)


def dfs(nums: List[int], i: int, curr_s: int, S: int, cache: List[Dict]) -> int:
    if i == len(nums):
        if curr_s == S:
            return 1
        return 0
    if curr_s in cache[i]:
        return cache[i][curr_s]
    add = dfs(nums, i + 1, curr_s + nums[i], S, cache)
    sub = dfs(nums, i + 1, curr_s - nums[i], S, cache)
    cache[i][curr_s] = add + sub
    return cache[i][curr_s]


def dp_2d_solution(nums: List[int], S: int) -> int:
    dp = [{} for _ in nums]

    for i, n in enumerate(nums):
        if i == 0:
            dp[i][-n] = dp[i].get(-n, 0) + 1
            dp[i][n] = dp[i].get(n, 0) + 1
        else:
            for prev_sum, prev_ways in dp[i - 1].items():
                for curr_sum in (prev_sum + n, prev_sum - n):
                    dp[i][curr_sum] = dp[i].get(curr_sum, 0) + prev_ways

    return dp[-1][S] if S in dp[-1] else 0


def test_one(nums: List[int], S: int, expected: int):
    print(nums)
    print(S)
    actual = Solution().findTargetSumWays(nums, S)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Expected {}, got {}!'.format(expected, actual))


if __name__ == '__main__':
    test_one([1, 1, 1, 1, 1], 5, 1)
    test_one([1, 1, 1, 1, 1], 3, 5)
    test_one([0, 0, 0, 0, 0, 0, 0, 0, 1], 1, 256)
