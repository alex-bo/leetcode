from typing import List


class Graph:

    def __init__(self, vertices_count: int):
        self.vertices_count = vertices_count
        self.adj = [set() for _ in range(vertices_count)]

    def add_edge(self, v: int, w: int):
        self.__check_vertex(v)
        self.__check_vertex(w)
        self.adj[v].add(w)
        self.adj[w].add(v)

    def __check_vertex(self, v: int):
        if 0 <= v < len(self.adj):
            return
        raise Exception('Given vertex is out of graph scope.')


class Digraph:

    def __init__(self, vertices_count: int):
        self.vertices = [set() for _ in range(vertices_count)]

    def add_edge(self, v_from: int, v_to: int):
        self.__check_vertex(v_from)
        self.__check_vertex(v_to)
        self.vertices[v_from].add(v_to)

    def __check_vertex(self, v: int):
        if 0 <= v < len(self.vertices):
            return
        raise Exception('Given vertex is out of graph scope.')


def dfs(g: Digraph, vs: List[int]) -> List[bool]:
    visited = [False for _ in range(len(g.vertices))]

    def visit(v: int):
        visited[v] = True
        for adj in g.vertices[v]:
            if not visited[adj]:
                visit(adj)

    for vertex in vs:
        if not visited[vertex]:
            visit(vertex)
    return visited
