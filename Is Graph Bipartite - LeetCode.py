from typing import List


class Solution:
    NOT_VISITED = 0
    SET_A = 1
    SET_B = 2

    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return False
        vs = [self.NOT_VISITED for _ in graph]
        not_visited = {i for i, v in enumerate(vs) if vs[i] == self.NOT_VISITED}

        while not_visited:
            v = next(iter(not_visited))
            not_visited.remove(v)
            q = [v]
            vs[v] = self.SET_A
            while q:
                v_from = q.pop(0)
                next_set = self.SET_A if vs[v_from] == self.SET_B else self.SET_B
                for v_to in graph[v_from]:
                    if vs[v_to] == self.NOT_VISITED:
                        vs[v_to] = next_set
                        not_visited.remove(v_to)
                        q.append(v_to)
                    elif vs[v_to] != next_set:
                        return False

        return True


def test_one(graph: List[List[int]], expected: bool):
    print(graph)
    actual = Solution().isBipartite(graph)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Expected {}, got {}!'.format(expected, actual))


if __name__ == '__main__':
    test_one([[1, 3], [0, 2], [1, 3], [0, 2]], True)
    test_one([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False)
    test_one([[4], [], [4], [4], [0, 2, 3]], True)
    test_one([[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
              [2, 4, 5, 6, 7, 8]], False)
