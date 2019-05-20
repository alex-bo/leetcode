from math import sqrt


def solution(A: int, B: int) -> int:
    cache = dict()
    return max(calculate(n, cache) for n in range(A, B+1))


def calculate(n: float, cache: dict) -> int:
    if (n % 1) != 0.0:
        return -1
    i = int(n)

    if i not in cache:
        cache[i] = calculate(sqrt(i), cache) + 1
    return cache[i]

    # return calculate(sqrt(i), cache) + 1

    # if i not in cache:
    #     r = calculate(sqrt(i), cache) + 1
    #     if r > 0:
    #         cache[i] = r
    #     else:
    #         return r
    # return cache[i]


def test_one(A: int, B: int, expected: int):
    print(A)
    print(B)
    actual = solution(A, B)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


def test():
    test_one(10, 20, 2)
    test_one(6000, 7000, 3)
    test_one(5000, 7000, 3)
    test_one(2, 20, 2)


def main():
    a = int(input('a: '))
    b = int(input('b: '))
    print(solution(a, b))


if __name__ == '__main__':
    test()
    main()
