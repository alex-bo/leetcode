

class Solution:

    def kInversePairs(self, n: int, k: int) -> int:
        return dp_solution(n, k, [[None for _ in range(k + 1)] for _ in range(n + 1)])


def dp_solution(n: int, k: int, cache: list) -> int:
    if n == 0:
        return 0
    if k == 0:
        return 1
    # if n < k:
    #     return 0
    if cache[n][k] is not None:
        return cache[n][k]
    res = 0
    for i in range(min(k, n - 1) + 1):
        res = (res + dp_solution(n - 1, k - i, cache)) % 1000000007
    cache[n][k] = res
    return res


if __name__ == '__main__':
    # TODO: complete this assessment
    print(Solution().kInversePairs(2, 1))
    # print(Solution().kInversePairs(3, 2))
    # print(Solution().kInversePairs(700, 1))
    print(Solution().kInversePairs(700, 700))
    # print(Solution().kInversePairs(1000, 1000))
