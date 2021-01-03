from collections import namedtuple
from typing import List


Doll = namedtuple('Doll', ['width', 'height'])


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        dolls = sorted(Doll(*e) for e in envelopes)
        return bottom_up_solution(dolls)


def bottom_up_solution(dolls: List[Doll]) -> int:
    dp = [1 for _ in dolls]
    for i in range(1, len(dp)):
        for j in range(i):
            if dp[j] + 1 > dp[i] and less_than(dolls[j], dolls[i]):
                dp[i] = dp[j] + 1
    return max(dp)


def patience_sort_solution(dolls: List[Doll]) -> int:
    # TODO: finished here
    pass


def less_than(left: Doll, right: Doll) -> bool:
    return left.width < right.width and left.height < right.height


if __name__ == '__main__':
    print(3, Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))
    print(1000, Solution().maxEnvelopes(list(zip(range(10000), range(10000)))))
