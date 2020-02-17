from typing import List


class Solution:

    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0

        left2right = get_candies(ratings)
        right2left = list(reversed(get_candies(list(reversed(ratings)))))

        # print('left2right={}'.format(left2right))
        # print('right2left={}'.format(right2left))
        # print('merged={}'.format(list(max(left, right) for left, right in zip(left2right, right2left))))

        return sum(
            (max(left, right) for left, right in zip(left2right, right2left))
        )


def get_candies(ratings: List[int]) -> List[int]:
    candies = [1 for _ in ratings]
    prev_r = None
    for i, r in enumerate(ratings):
        if i > 0 and r > prev_r:
            candies[i] = candies[i - 1] + 1
        prev_r = r
    return candies


def test_one(ratings: List[int], expected: int):
    print(ratings)
    actual = Solution().candy(ratings)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


def test():
    test_one([1, 2, 87, 87, 87, 2, 1], 13)


if __name__ == '__main__':
    test()

