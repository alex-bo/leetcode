

# Definition for a binary tree node.
from typing import List, Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        path = []
        find_target(root, target, path)
        result = []
        prev = None
        for i, node in enumerate(path):
            result.extend(find_kth(node, K - i, prev))
            prev = node
        return result


def find_target(node: TreeNode, target: TreeNode, path: List[TreeNode]) -> bool:
    if not node:
        return False
    if node.val == target.val or find_target(node.left, target, path) or find_target(node.right, target, path):
        path.append(node)
        return True
    return False


def find_kth(node: TreeNode, k: int, block: TreeNode) -> List[int]:
    if not node or (block and node.val == block.val):
        return []
    if k == 0:
        return [node.val]
    res = find_kth(node.left, k - 1, block)
    res.extend(find_kth(node.right, k - 1, block))
    return res


if __name__ == '__main__':
    pass
