

class Solution:

    def reverse(self, x: int) -> int:
        val = str(x).lstrip('-')[::-1]
        if x < 0:
            val = '-' + val
        res = int(val)
        if MIN_VALUE < res < MAX_VALUE:
            return res
        return 0


MAX_VALUE = 2**31 - 1
MIN_VALUE = -2**31


def test_one(x: int, expected: int):
    print(x)
    actual = Solution().reverse(x)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


def test():
    test_one(123, 321)
    test_one(-123, -321)
    test_one(1534236469, 0)


def main():
    x = int(input('x: '))
    print(Solution().reverse(x))


if __name__ == '__main__':
    test()
    # main()
