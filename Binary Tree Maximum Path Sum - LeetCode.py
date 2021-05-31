# Definition for a binary tree node.
from typing import Tuple, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return max(solution(root))


def solution(node: TreeNode) -> Tuple[int, int, int]:
    if not node:
        return -2**32, -2**32, -2**32

    left_with_root, left_without_root, left_both = solution(node.left)
    right_with_root, right_without_root, right_both = solution(node.right)

    return max(
        left_with_root + node.val,
        right_with_root + node.val,
        node.val
    ), max(
        left_without_root,
        right_without_root,
        left_with_root,
        right_with_root
    ), max(
        left_both,
        right_both,
        left_with_root + node.val + right_with_root
    )
