from typing import List, Optional
from heapq import heappop, heappush


class MyListNode:
    def __init__(self, n):
        self.val = n.val
        self.next = n.next

    def __lt__(self, other: 'MyListNode') -> bool:
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[MyListNode]) -> MyListNode:
        heap = []
        for n in lists:
            if n:
                heappush(heap, MyListNode(n))
        root_node = get_min_node(heap)
        curr_node = root_node
        while curr_node:
            next_node = get_min_node(heap)
            curr_node.next = next_node
            curr_node = next_node
        return root_node


def get_min_node(heap: List[MyListNode]) -> Optional[MyListNode]:
    if not heap:
        return None
    min_node = heappop(heap)
    if min_node.next:
        heappush(heap, MyListNode(min_node.next))
    return min_node

