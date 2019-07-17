from typing import List


class Solution:

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        """Find pattern and calculate Nth transformation."""
        if N == 0:
            return cells
        if N == 1:
            return transform(cells)
        patterns = [transform(cells)]
        for i in range(2, N + 1):
            transformed = transform(patterns[-1])
            if transformed in patterns:
                return patterns[(N - i) % len(patterns)]
            patterns.append(transformed)
        return patterns[-1]

    def prisonAfterNDaysNotOptimized(self, cells: List[int], N: int) -> List[int]:
        cells_from = cells
        cells_to = [c for c in cells]
        for _ in range(N):
            cells_to[0] = 0
            cells_to[-1] = 0
            for i in range(1, len(cells) - 1):
                cells_to[i] = 1 if cells_from[i-1] == cells_from[i+1] else 0
            print(cells_to)
            cells_from, cells_to = cells_to, cells_from
        return cells_from


def transform(cells: List[int]) -> List[int]:
    transformed = [0]
    for i in range(1, len(cells) - 1):
        transformed.append(1 if cells[i - 1] == cells[i + 1] else 0)
    transformed.append(0)
    return transformed


def test():
    test_one([0, 1, 0, 1, 1, 0, 0, 1], 0, [0, 1, 0, 1, 1, 0, 0, 1])
    test_one([0, 1, 0, 1, 1, 0, 0, 1], 1, [0, 1, 1, 0, 0, 0, 0, 0])
    test_one([0, 1, 0, 1, 1, 0, 0, 1], 7, [0, 0, 1, 1, 0, 0, 0, 0])
    test_one([1, 0, 0, 1, 0, 0, 1, 0], 1000000000, [0, 0, 1, 1, 1, 1, 1, 0])


def test_one(cells: List[int], N: int, expected: List[int]) -> bool:
    print(cells)
    print(N)
    actual = Solution().prisonAfterNDays(cells, N)
    if actual == expected:
        print('OK')
        return True
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))
        return False


if __name__ == '__main__':
    test()
