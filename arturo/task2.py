from typing import List


def solution(T: List[int]) -> str:
    max_alt = 0
    max_season = None
    seasons = ['WINTER', 'SPRING', 'SUMMER', 'AUTUMN']
    for i, season in enumerate(seasons):
        start = (len(T) // len(seasons)) * i
        stop = start + (len(T) // len(seasons))
        alt = max(T[start:stop]) - min(T[start:stop])
        if alt > max_alt:
            max_alt, max_season = alt, season
    return max_season


def test_one(T: List[int], expected: str):
    print(T)
    actual = solution(T)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


def test():
    test_one([-3, -14, -5, 7, 8, 42, 8, 3], 'SUMMER')
    test_one([2, -3, 3, 1, 10, 8, 2, 5, 13, -5, 3, -18], 'AUTUMN')
    test_one([20, -3, -30, 1, 10, 8, 2, 5, 13, -5, 3, -18], 'WINTER')


if __name__ == '__main__':
    test()
