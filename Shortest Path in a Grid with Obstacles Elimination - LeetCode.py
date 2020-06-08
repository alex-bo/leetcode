from collections import namedtuple
from typing import List

Position = namedtuple('Position', ['i', 'j'])


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        return bfs(grid, k)


def bfs(grid: List[List[int]], k: int) -> int:
    if len(grid) == 1 and len(grid[0]) == 1:
        return 0
    visited = {Position(0, 0): k}
    queue1 = [Position(0, 0)]
    queue2 = []
    steps = 1
    target = Position(len(grid) - 1, len(grid[0]) - 1)

    while queue1:
        pos = queue1.pop()
        next_poss = [
            Position(pos.i + 1, pos.j),
            Position(pos.i - 1, pos.j),
            Position(pos.i, pos.j + 1),
            Position(pos.i, pos.j - 1),
        ]
        for next_pos in next_poss:
            if 0 <= next_pos.i < len(grid) and 0 <= next_pos.j < len(grid[0]):
                next_k = visited[pos]
                if grid[next_pos.i][next_pos.j] == 1:
                    next_k -= 1
                if next_pos == target:
                    return steps
                if next_k >= 0 and (next_pos not in visited or visited[next_pos] < visited[pos]):
                    queue2.append(next_pos)
                    visited[next_pos] = next_k
        if not queue1:
            queue1, queue2 = queue2, queue1
            steps += 1
    return -1


def test(grid: List[List[int]], k: int, expected: int):
    print(grid)
    print(k)
    actual = Solution().shortestPath(grid, k)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Expected {}, got {}'.format(expected, actual))


if __name__ == '__main__':
    test([[0, 0, 0],
          [1, 1, 0],
          [0, 0, 0],
          [0, 1, 1],
          [0, 0, 0]], 1, 6)
    test([[0, 1, 1],
          [1, 1, 1],
          [1, 0, 0]], 1, -1)
    test([[0]], 1, 0)
