from typing import List


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        d = build_epsilon_transitions(p)
        return recognize(s, p, d)


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


def recognize(s: str, p: str, g: Digraph) -> bool:
    states = []
    for v, visited in enumerate(dfs(g, [0])):
        if visited:
            states.append(v)

    for i, c in enumerate(s):
        matches = []
        for state in states:
            if state == len(p):
                continue
            # travel ahead one state if match or [.]
            if p[state] == c or p[state] == '.':
                matches.append(state+1)
        states = []
        for v, visited in enumerate(dfs(g, matches)):
            if visited:
                states.append(v)
        if not states:
            break
    if len(p) in states:
        return True
    return False


def build_epsilon_transitions(p: str) -> Digraph:
    g = Digraph(len(p) + 1)
    for i, c in enumerate(p):
        if c == '*':
            if i > 0:
                # can travel back and forth within combination of [character] <-> [*]
                g.add_edge(i, i-1)
                g.add_edge(i-1, i)
                # and only ahead to the next character
                g.add_edge(i, i+1)
            else:
                raise Exception('Invalid pattern, asterisk does not follow any character.')
    return g


def test_one(s: str, p: str, expected: bool):
    print(s)
    print(p)
    actual = Solution().isMatch(s, p)
    if actual == expected:
        print('OK')
    else:
        print('WRONG!')


def test():
    test_one('aa', 'a', False)
    test_one('aa', 'a*', True)
    test_one('ab', '.*', True)
    test_one('aab', 'c*a*b', True)
    test_one('mississippi', 'mis*is*p*.', False)


if __name__ == '__main__':
    test()
