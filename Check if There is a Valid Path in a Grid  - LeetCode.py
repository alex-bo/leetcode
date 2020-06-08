from collections import namedtuple
from typing import List, Set

Position = namedtuple('Position', ['i', 'j'])


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        return dfs(Position(0, 0), Position(len(grid) - 1, len(grid[-1]) - 1), grid, set())


def dfs(pos: Position, target: Position, grid: List[List[int]], visited: Set[Position]) -> bool:
    if pos == target:
        return True
    for step in next_steps(pos, grid):
        if step in visited:
            continue
        # print(step)
        visited.add(step)
        if dfs(step, target, grid, visited):
            return True
    return False


def next_steps(pos: Position, grid: List[List[int]]) -> List[Position]:
    steps = []
    val = grid[pos.i][pos.j]
    way_up = (2, 5, 6)
    way_down = (2, 3, 4)
    way_left = (1, 3, 5)
    way_right = (1, 4, 6)

    # left
    if pos.j > 0 and val in way_left:
        p = Position(pos.i, pos.j - 1)
        if grid[p.i][p.j] in way_right:
            steps.append(p)

    # right
    if pos.j < (len(grid[pos.i]) - 1) and val in way_right:
        p = Position(pos.i, pos.j + 1)
        if grid[p.i][p.j] in way_left:
            steps.append(p)

    # up
    if pos.i > 0 and val in way_up:
        p = Position(pos.i - 1, pos.j)
        if grid[p.i][p.j] in way_down:
            steps.append(p)

    # down
    if pos.i < (len(grid) - 1) and val in way_down:
        p = Position(pos.i + 1, pos.j)
        if grid[p.i][p.j] in way_up:
            steps.append(p)

    return steps


def test(grid: List[List[int]], expected: bool):
    print(grid)
    actual = Solution().hasValidPath(grid)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}'.format(actual, expected))


if __name__ == '__main__':
    test([[1, 2, 1], [1, 2, 1]], False)
    test([[2, 4, 3], [6, 5, 2]], True)
    test([[1, 1, 1, 1, 1, 1, 3]], True)
    test([[1, 1, 2]], False)
    test([[1]], True)
