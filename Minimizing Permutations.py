from typing import Tuple, List


def minOperations(arr: List[int]):
    graph = {}
    build_graph(graph, tuple(arr))
    return bfs(graph, tuple(arr), tuple(sorted(arr)))


def build_graph(graph: dict, src: Tuple[int]):
    i = 0
    if src in graph:
        return
    graph[src] = set()
    while i < len(src):
        i, dst = reverse(src, i)
        if dst and dst != src:
            graph[src].add(dst)
            build_graph(graph, dst)


def reverse(src: Tuple[int], i: int) -> Tuple[int, Tuple[int]]:
    if i >= len(src) - 1:
        return len(src), src
    reverse_sequence = [src[i]]
    sign = 1 if src[i] < src[i + 1] else -1
    for j in range(i + 1, len(src)):
        if src[j] != (src[i] + (j - i) * sign):
            break
        reverse_sequence.append(src[j])
    return i + len(reverse_sequence), tuple(
        src[:i] +
        tuple(reverse_sequence[::-1]) +
        src[i + len(reverse_sequence):]
    )


def bfs(graph: dict, src: Tuple[int], dst: Tuple[int]) -> int:
    queue = [src]
    visited = {src: 0}
    while queue:
        frm = queue.pop(0)
        for nxt in graph[frm]:
            if nxt in visited:
                continue
            if nxt == dst:
                return visited[frm] + 1
            queue.append(nxt)
            visited[nxt] = visited[frm] + 1
    return 0


if __name__ == '__main__':
    print(2, minOperations([3, 1, 2]))
    print(1, minOperations([1, 2, 5, 4, 3]))
    print(3, minOperations([2, 1, 4, 3, 6, 5]))
    print(2, minOperations([6, 5, 4, 1, 2, 3]))
