from typing import List


class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        # return recursive_match(s, p, 0, 0)
        # NFA
        digraph = build_epsilon_transition_digraph(p)
        return recognizes(digraph, s, p)


# NFA simulation
def recognizes(digraph: 'Digraph', s: str, p: str):
    # states reachable from start by epsilon-transitions
    pc = []
    dfs = DirectedDFS(digraph, [0])
    for v in range(digraph.vertices_count):
        if dfs.visited(v):
            pc.append(v)

    for i in range(len(s)):
        # states reachable after scanning past s[i]
        match = []
        for v in pc:
            if v == len(p):
                continue
            if p[v] == s[i] or p[v] == '?' or p[v] == '*':
                match.append(v + 1)

        # follow epsilon transition
        pc = []
        dfs = DirectedDFS(digraph, match)
        for v in range(digraph.vertices_count):
            if dfs.visited(v):
                pc.append(v)

    for v in pc:
        if v == len(p):
            return True
    return False


# NFA construction
def build_epsilon_transition_digraph(p: str) -> 'Digraph':
    digraph = Digraph(len(p) + 1)  # last state is end state
    for i in range(len(p)):
        if p[i] == '(' or p[i] == ')':
            digraph.add_edge(i, i + 1)
        if p[i] == '*':
            digraph.add_edge(i, i + 1)
            digraph.add_edge(i + 1, i)
    return digraph


class Digraph:
    # states are numerical numbers start from 0 to V-1
    def __init__(self, vertices_count: int):
        """
        create empty graph with V vertices
        """
        self.vertices_count = vertices_count
        # Adjacency-list, maintain vertex-indexed array of lists.
        self.adj = [[] for _ in range(vertices_count)]

    def add_edge(self, v, w):
        """
        add a directed edge v->w
        """
        self.adj[v].append(w)


class DirectedDFS:
    def __init__(self, digraph: Digraph, s: List[int]):
        """
        :type digraph: Digraph
        :type s: List[int] start states
        """
        self.__marked = [False for _ in range(digraph.vertices_count)]
        for v in s:
            if not self.__marked[v]:
                self.__dfs(digraph, v)

    def __dfs(self, digraph: Digraph, v: int):
        """
        recursive DFS does the work
        """
        self.__marked[v] = True
        for w in digraph.adj[v]:
            if not self.__marked[w]:
                self.__dfs(digraph, w)

    def visited(self, v: int):
        """
        client can ask whether any vertex is reachable from s
        """
        return self.__marked[v]


def recursive_match(s: str, p: str, si: int, pi: int) -> bool:
    """
    Brute Force recursive solution
    """
    # end of s
    if len(s) <= si:
        # end of p or only *'s left
        if len(p) <= pi or len(p[pi:].replace('*', '')) == 0:
            return True
        return False

    # end of p
    if len(p) <= pi:
        return False

    # *
    if p[pi] == '*':
        if recursive_match(s, p, si+1, pi):
            return True
        if recursive_match(s, p, si+1, pi+1):
            return True
        if recursive_match(s, p, si, pi+1):
            return True
        return False

    # ?
    if p[pi] == '?':
        return recursive_match(s, p, si+1, pi+1)

    # character
    if s[si] == p[pi]:
        return recursive_match(s, p, si+1, pi+1)
    return False


def test_one(s: str, p: str, expected: bool):
    print(s)
    print(p)
    actual = Solution().isMatch(s, p)
    if actual == expected:
        print('OK')
    else:
        print('WRONG!')


def test():
    test_one('cb', '?a', False)
    test_one('aa', '*', True)
    test_one('aa', 'a', False)
    test_one('adceb', 'a*b', True)
    test_one('acdcb', 'a*c?b', False)
    test_one('adceb', '*a*b', True)
    test_one('aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab', '*ab***ba**b*b*aaab*b', True)


if __name__ == '__main__':
    # pass
    test()
