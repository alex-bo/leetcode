from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def minDepth(self, root: TreeNode) -> int:
        """DFS"""

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            if not node.left:
                return dfs(node.right) + 1
            if not node.right:
                return dfs(node.left) + 1
            return min(dfs(node.left), dfs(node.right)) + 1

        return dfs(root)
