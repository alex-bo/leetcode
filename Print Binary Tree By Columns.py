from pprint import pprint
from typing import List

from binarytree import tree, Node

"""
Example:

tree:
    _____2___
   /         \
  8          _11
 / \        /   \
6   4      10    0
     \
      12

result:
    [
        [6],
        [8],
        [2, 4, 10],
        [11, 12],
        [0]
    ]

"""


def print_tree(tr: Node) -> List[List[int]]:
    q = []
    dct = {}
    q.append((tr, 0))
    while q:
        node, i = q.pop(0)
        if i not in dct:
            dct[i] = []
        dct[i].append(node.value)
        if node.left:
            q.append((node.left, i - 1))
        if node.right:
            q.append((node.right, i + 1))

    res = []
    for i in range(min(dct.keys()), max(dct.keys()) + 1):
        res.append(dct[i])
    return res


def main():
    tr = tree()
    print('-----------------------------------------------------')
    print('tr {}:'.format(len(tr)))
    print(tr)
    res = print_tree(tr)
    # print('{} {}'.format(sum(len(i) for i in res), res))
    pprint(res)


if __name__ == '__main__':
    main()

