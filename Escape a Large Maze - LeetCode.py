from collections import namedtuple
from typing import List

Position = namedtuple('Position', ['x', 'y'])

GRAPH_EDGE = 10 ** 6


class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked_set = set()
        for x, y in blocked:
            blocked_set.add(Position(x, y))
        return (
            bfs(Position(*source), Position(*target), blocked_set) and
            bfs(Position(*target), Position(*source), blocked_set)
        )


def bfs(start: Position, target: Position, blocked: set) -> bool:
    queue = [start]
    visited = {start}
    while queue:
        curr_pos = queue.pop(0)
        next_poss = [
            Position(curr_pos.x - 1, curr_pos.y),
            Position(curr_pos.x + 1, curr_pos.y),
            Position(curr_pos.x, curr_pos.y - 1),
            Position(curr_pos.x, curr_pos.y + 1),
        ]
        for next_pos in next_poss:
            if next_pos in visited or next_pos in blocked or not check_boundaries(next_pos):
                continue
            if next_pos == target:
                return True
            queue.append(next_pos)
            visited.add(next_pos)
            if len(queue) >= len(blocked):
                return True
    return False


def check_boundaries(pos: Position) -> bool:
    return 0 <= pos.x < GRAPH_EDGE and 0 <= pos.y < GRAPH_EDGE


def test(blocked: List[List[int]], source: List[int], target: List[int], expected: bool):
    print(blocked)
    print(source)
    actual = Solution().isEscapePossible(blocked, source, target)
    if expected == actual:
        print('OK')
    else:
        print('WRONG! Expected {}, got {}!'.format(expected, actual))


if __name__ == '__main__':
    test([[0, 1], [1, 0]], [0, 0], [0, 2], False)
    test([], [0, 0], [999999, 999999], True)
