from typing import List


class Solution:

    def jump(self, s: List[int]) -> int:
        dp = [float('inf')] * len(s)
        dp[0] = 0
        for i in range(len(s)):
            for j in range(i + 1, min(i + s[i] + 1, len(dp))):
                dp[j] = min(
                    dp[j],
                    dp[i] + 1
                )
        return int(dp[-1])


def test_one(s: List[int], expected: int) -> bool:
    print(s)
    actual = Solution().jump(s)
    if actual == expected:
        print('OK')
        return True
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))
        return False


def test():
    test_one([2, 3, 1, 1, 4], 2)


if __name__ == '__main__':
    # TODO: submit solution
    test()
