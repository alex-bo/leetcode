from collections import namedtuple
from typing import List

Position = namedtuple('Position', ['i', 'j'])


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        return bfs(grid, k)


def bfs(grid: List[List[int]], k: int) -> int:
    visited = {Position(0, 0): k}
    queue1 = [visited]
    queue2 = []
    steps = 0

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
                visited[next_pos] = max(next_k, visited.get(next_pos, 0))
                if visited[next_pos] > 0:
                    queue2.append(next_pos)
        steps += 1
        if not queue1:
            queue1, queue2 = queue2, queue1
    return -1

