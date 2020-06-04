from typing import List


class Solution:

    def __init__(self):
        self.visited = None
        self.vertex_ids = None
        self.vertex_low = None
        self.critical_conns = None
        self.id = 0

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = build_graph(n, connections)
        self.visited = [False for _ in range(n)]
        self.vertex_ids = [-1 for _ in range(n)]
        self.vertex_low = [-1 for _ in range(n)]
        self.critical_conns = []
        self.id = 0
        self.dfs(0, -1, graph)
        return self.critical_conns

    def dfs(self, v: int, parent: int, graph: List[List[int]]):
        self.vertex_ids[v] = self.id
        self.vertex_low[v] = self.id
        self.id += 1
        self.visited[v] = True
        for w in graph[v]:
            if w == parent:
                continue
            if self.visited[w]:
                # found alternative way from w to v
                # entire SCC (strongly connected component) reduces to the lowest vertex ID
                self.vertex_low[v] = min(self.vertex_low[v], self.vertex_ids[w])
            else:
                self.dfs(w, v, graph)
                # reduce current low to the lowest found so far in SCC
                self.vertex_low[v] = min(self.vertex_low[v], self.vertex_low[w])
                if self.vertex_ids[v] < self.vertex_low[w]:
                    self.critical_conns.append([v, w])


def build_graph(n: int, connections: List[List[int]]) -> List[List[int]]:
    vertices = [[] for _ in range(n)]
    for v1, v2 in connections:
        vertices[v1].append(v2)
        vertices[v2].append(v1)
    return vertices


def tarjan_scc_algo_solution(n: int, connections: List[List[int]]) -> List[List[int]]:
    graph = build_graph(n, connections)
    visited = [False for _ in range(n)]
    return dfs(-1, 0, graph, [-1 for _ in range(n)], visited, 0)


def dfs(from_v: int, to_v: int, graph: List[List[int]], components: List[int],
        visited: List[bool], comp_id: int) -> List[List[int]]:
    if visited[to_v]:
        return []
    critical = []
    components[to_v] = comp_id
    visited[to_v] = True
    for v in graph[to_v]:
        if v == from_v:
            continue
        critical.extend(dfs(to_v, v, graph, components, visited, comp_id + 1))
        components[to_v] = min(components[to_v], components[v])
        if components[to_v] != components[v]:
            critical.append([to_v, v])
    return critical


def brute_force_solution(n: int, connections: List[List[int]]) -> List[List[int]]:
    graph = build_graph(n, connections)
    critical = [[] for _ in range(n)]

    for v1, conns in enumerate(graph):
        for v2 in conns:
            if v1 > v2:
                continue
            if not bfs(v1, v2, graph):
                critical[v1].append(v2)
    res = []
    for v1, conns in enumerate(critical):
        for v2 in conns:
            res.append([v1, v2])
    return res


def bfs(v_from: int, v_to: int, graph: List[List[int]]) -> bool:
    visited = [False for _ in range(len(graph))]
    queue = [v_from]
    visited[v_from] = True
    while queue:
        v1 = queue.pop(0)
        for v2 in graph[v1]:
            # ignore direct path
            if v1 == v_from and v2 == v_to:
                continue
            if v2 == v_to:
                return True
            if not visited[v2]:
                queue.append(v2)
                visited[v2] = True
    return False


def test(n: int, connections: List[List[int]], expected: List[List[int]]):
    print(n)
    print(connections)
    actual = Solution().criticalConnections(n, connections)
    if expected == actual:
        print('OK')
    else:
        print('WRONG! Expected {}, got {}!'.format(expected, actual))


if __name__ == '__main__':
    test(4, [[0, 1], [1, 2], [2, 3], [3, 0]], [])
    test(4, [[0, 1], [0, 2], [0, 3]], [[0, 1], [0, 2], [0, 3]])
    test(4, [[0, 1], [1, 2], [2, 0], [1, 3]], [[1, 3]])
    test(2, [[1, 0]], [[0, 1]])
    test(6, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]], [[1, 3]])
    test(10, [[1, 0], [2, 0], [3, 0], [4, 1], [5, 3], [6, 1], [7, 2], [8, 1], [9, 6], [9, 3], [3, 2], [4, 2], [7, 4],
              [6, 2], [8, 3], [4, 0], [8, 6], [6, 5], [6, 3], [7, 5], [8, 0], [8, 5], [5, 4], [2, 1], [9, 5], [9, 7],
              [9, 4], [4, 3]], [])
