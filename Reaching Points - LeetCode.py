

class Solution:

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """Recursive, going down"""

        def solve(x: int, y: int) -> bool:
            if x < sx or y < sy:
                return False
            if x == sx:
                if (y - sy) % x == 0:
                    return True
                return False
            if y == sy:
                if (x - sx) % y == 0:
                    return True
                return False
            return solve(x - y, y) or solve(x, y - x)

        return solve(tx, ty)


def test():
    test_one(1, 1, 3, 5, True)
    test_one(1, 1, 2, 2, False)
    test_one(35, 13, 455955547, 420098884, False)
    test_one(1, 1, 1000000000, 1, True)
    test_one(10, 4, 10, 20, False)


def test_one(sx: int, sy: int, tx: int, ty: int, expected: bool) -> bool:
    print(sx, sy)
    print(tx, ty)
    actual = Solution().reachingPoints(sx, sy, tx, ty)
    if actual == expected:
        print('OK')
        return True
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))
        return False


if __name__ == '__main__':
    test()
