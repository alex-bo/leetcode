from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head
        new_head = None
        prev = None
        curr = head
        left_parent, left = None, None
        i = 0
        while curr:
            i += 1
            if i == 1:
                # remember left node to swap
                left_parent, left = prev, curr
            elif i == k:
                # reverse k-group
                curr = left
                for j in range(k, 1, -1):
                    left = push_down(left, j)
                if left_parent:
                    left_parent.next = left
                if not new_head:
                    new_head = left
                i = 0
            # move next
            prev = curr
            curr = curr.next
        return new_head or head

    def reverse_k_first_elements(self, head: ListNode, k: int) -> ListNode:
        while k > 1:
            head = push_down(head, k)
            k -= 1
        return head


def push_down(head: ListNode, k: int) -> ListNode:
    """
    For head = 1 -> 2 -> 3 -> 4 and k = 3, push down head k times to 2 -> 3 -> 1 -> 4

    :param head: node 1
    :param k: number of times to push down
    :return: node 2
    """
    if k <= 1 or not head:
        return head
    head = push_down_node(head)
    head.next = push_down(head.next, k - 1)
    return head


def push_down_node(node: ListNode) -> ListNode:
    """
    Convert 1 -> 2 -> 3 to 2 -> 1-> 3

    :param node: node 1
    :return: node 2
    """
    if not node or not node.next:
        return node
    one = node
    two = one.next
    three = two.next

    two.next = one
    one.next = three

    return two


def test_one(lst: List[int], k: int, expected: List[int]):
    print(lst)
    print(k)
    actual = list_node_to_list(Solution().reverseKGroup(list_to_list_node(lst), k))
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


def test_list_conversions():
    print('Testing list conversion...')
    expected = list(range(10))
    actual = list_node_to_list(list_to_list_node(expected))
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


def test_push_down(lst: List[int], k: int, expected: List[int]):
    # print(lst)
    print(k)
    head = list_to_list_node(lst)
    head = push_down(head, k)
    actual = list_node_to_list(head)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


def test_push_downs():
    print('Testing push down...')
    lst = [i for i in range(1, 6)]
    test_push_down(lst, 1, [1, 2, 3, 4, 5])
    test_push_down(lst, 2, [2, 1, 3, 4, 5])
    test_push_down(lst, 3, [2, 3, 1, 4, 5])
    test_push_down(lst, 4, [2, 3, 4, 1, 5])
    test_push_down(lst, 5, [2, 3, 4, 5, 1])


def list_to_list_node(lst: List[int]) -> ListNode:
    head = None
    prev = None
    for x in lst:
        node = ListNode(x)
        if not head:
            head = node
        if prev:
            prev.next = node
        prev = node
    return head


def list_node_to_list(head: ListNode) -> List[int]:
    lst = []
    cur = head
    while cur:
        lst.append(cur.val)
        cur = cur.next
    return lst


def test():
    test_one([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5])
    test_one([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5])
    test_one([1, 2, 3, 4, 5, 6, 7, 8], 4, [4, 3, 2, 1, 8, 7, 6, 5])


if __name__ == '__main__':
    test()
    # test_list_conversions()
    # test_push_downs()
