

class Solution:

    def intToRoman(self, num: int) -> str:
        res = ''
        symbols = [
            ('I', 'V', 'X'),
            ('X', 'L', 'C'),
            ('C', 'D', 'M'),
            ('M', None, None),
        ]
        i = 0
        for d in reversed(str(num)):
            digit = int(d)
            if digit > 0:
                if i >= len(symbols):
                    raise Exception('Unexpectedly large number.')
                one, five, ten = symbols[i]
                res = convert_digit(digit, one, five, ten) + res
            i += 1
        return res


def convert_digit(digit: int, one: str, five: str, ten: str) -> str:
    if digit < 0 or digit > 9:
        raise ValueError('Invalid digit.')
    if digit < 4:
        return one * digit

    if not five and not ten:
        raise Exception('Five and ten symbols are not set, conversion not supported.')

    if digit <= 5:
        return one * (5 - digit) + five
    if digit < 9:
        return five + one * (digit - 5)
    return one + ten


def test_one(num: int, expected: str):
    print(num)
    print(expected)
    actual = Solution().intToRoman(num)
    if expected == actual:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


def test():
    test_one(3, 'III')
    test_one(4, 'IV')
    test_one(9, 'IX')
    test_one(58, 'LVIII')


if __name__ == '__main__':
    test()


