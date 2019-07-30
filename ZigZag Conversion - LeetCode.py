class Solution:

    def convert(self, s: str, numRows: int) -> str:
        rows_count = numRows
        cols_count = numRows * (len(s) // numRows + 1) * 2
        arr = [[] for _ in range(rows_count)]
        letters = list(s)
        for j in range(cols_count):
            if not letters:
                break
            if (j % 2) == 0:
                rng = range(rows_count)
            else:
                rng = range(rows_count - 2, 0, -1)
            for i in rng:
                if not letters:
                    break
                while len(arr[i]) <= j:
                    arr[i].append('')
                arr[i][j] = letters.pop(0)

        res = []
        for i in range(rows_count):
            for j in range(cols_count):
                if len(arr[i]) <= j:
                    break
                if arr[i][j]:
                    res.append(arr[i][j])
        return ''.join(res)


def test_one(s: str, numRows: int, expected: str):
    print(s)
    print(numRows)
    actual = Solution().convert(s, numRows)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


def test():
    test_one('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR')
    test_one('PAYPALISHIRING', 4, 'PINALSIGYAHRPI')
    test_one('A', 2, 'A')
    test_one('ABC', 1, 'ABC')


if __name__ == '__main__':
    test()
