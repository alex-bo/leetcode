from time import time
from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, a: List[int], l: int, m: int) -> int:
        l_dp = calc_dp(a, l)
        m_dp = calc_dp(a, m)
        mx = -1
        for i in range(l-1, len(a)):
            for j in range(m-1, len(a)):
                if (i-l) < j < (i+m):
                    continue
                mx = max(mx, l_dp[i] + m_dp[j])
        return mx


def calc_dp(a: List[int], l: int) -> List[int]:
    dp = [-1 for _ in a]
    dp[l-1] = sum(a[:l])
    for i in range(l, len(a)):
        dp[i] = dp[i-1] + a[i] - a[i-l]
    return dp


def main():
    test([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2, 20)
    test([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2, 29)
    test([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3, 31)


def test(a: List[int], l: int, m: int, expected: int) -> None:
    print(a)
    print(l)
    print(m)
    actual = Solution().maxSumTwoNoOverlap(a, l, m)
    if actual == expected:
        print('OK')
    else:
        print('WRONG!')
        raise Exception('Expected {}, got {}'.format(expected, actual))


if __name__ == '__main__':
    main()
