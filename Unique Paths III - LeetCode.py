from collections import namedtuple
from typing import List, Set

Position = namedtuple('Position', ['i', 'j'])


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = None
        zeros = 2  # include 1 and 2
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if c == 1:
                    start = Position(i, j)
                elif c == 0:
                    zeros += 1
        if not start:
            return 0
        return dfs(grid, {start}, start, zeros)


def dfs(grid: List[List[int]], path: Set[Position], p: Position, zeros: int) -> int:
    if p.i < 0 or p.j < 0 or p.i >= len(grid) or p.j >= len(grid[0]):
        return 0
    if grid[p.i][p.j] == -1:
        return 0
    if grid[p.i][p.j] == 2:
        # if len(path) == zeros:
        #     print(path)
        return 1 if len(path) == zeros else 0

    res = 0
    for nxt_p in (left(p), right(p), up(p), down(p)):
        if nxt_p in path:
            continue
        path.add(nxt_p)
        res += dfs(grid, path, nxt_p, zeros)
        path.remove(nxt_p)
    return res


def left(p: Position) -> Position:
    return Position(p.i, p.j - 1)


def right(p: Position) -> Position:
    return Position(p.i, p.j + 1)


def up(p: Position) -> Position:
    return Position(p.i - 1, p.j)


def down(p: Position) -> Position:
    return Position(p.i + 1, p.j)


def print_grid(grid: List[List[int]]):
    for r in grid:
        print(r)


def test_one(grid: List[List[int]], expected: int):
    print_grid(grid)
    actual = Solution().uniquePathsIII(grid)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}!'.format(actual, expected))


def test():
    test_one([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2)
    test_one([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4)
    test_one([[0, 1], [2, 0]], 0)


if __name__ == '__main__':
    test()

