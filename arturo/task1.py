# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(name: str, surname: str, age: int) -> str:
    return ''.join((name[:2], surname[:2], str(age)))


def test_one(name: str, surname: str, age: int, expected: str):
    print(name)
    print(surname)
    print(age)
    actual = solution(name, surname, age)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


def test():
    test_one('John', 'Firelord', 8, 'JoFi8')
    test_one('Alex', 'Test', 123, 'AlTe123')
    test_one('Hello', 'There', 99, 'HeTh99')


if __name__ == '__main__':
    test()
