import functools


def count_patterns_from(firstPoint: str, length: int) -> int:
    visit_rules = init_visit_rules()
    graph = init_graph()
    found_patterns = set()

    if length > graph.vertices_count:
        return 0

    @functools.lru_cache(None)
    def dfs(v: int, depth: int, curr_path: str):
        depth += 1
        if depth > length:
            return

        curr_path = curr_path + str(v)
        if depth == length:
            found_patterns.add(curr_path)
        else:
            for w in graph.adj[v]:
                # if cannot be visited before adjacent vertices
                if w in visit_rules[v] and str(visit_rules[v][w]) not in curr_path:
                    continue

                # if already visited
                if str(w) in curr_path:
                    continue

                dfs(w, depth, curr_path)

    dfs(ord(firstPoint) - ord('A'), 0, '')
    return len(found_patterns)


class Graph:

    def __init__(self, vertices_count: int):
        self.vertices_count = vertices_count
        self.adj = [set() for _ in range(vertices_count)]

    def add_edge(self, v: int, w: int):
        self.adj[v].add(w)
        self.adj[w].add(v)


def init_graph() -> Graph:
    graph = Graph(9)
    for v in range(graph.vertices_count):
        for w in range(graph.vertices_count):
            if v != w:
                graph.add_edge(v, w)
    return graph


def init_visit_rules() -> list:
    return [
        # from -> to -> if visited...
        {
            2: 1,
            8: 4,
            6: 3,
        },
        {
            7: 4,
        },
        {
            0: 1,
            6: 4,
            8: 5,
        },
        {
            5: 4,
        },
        {},
        {
            3: 4,
        },
        {
            0: 3,
            2: 4,
            8: 7,
        },
        {
            1: 4,
        },
        {
            0: 4,
            2: 5,
            6: 7,
        },
    ]


def test_one(firstPoint: str, length: int, expected: int) -> bool:
    print(firstPoint)
    print(length)
    actual = count_patterns_from(firstPoint, length)
    if actual == expected:
        print('OK')
        return True
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))
        return False


def test():
    test_one('A', 10, 0)
    test_one('A', 0, 0)
    test_one('E', 14, 0)
    test_one('B', 1, 1)
    test_one('C', 2, 5)
    test_one('E', 2, 8)
    test_one('E', 4, 256)



if __name__ == '__main__':
    r = minimumDays(5, 5, [
        [1,0,0,0,0],
        [0,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,0,0,0,1],
    ])
    print(r)
