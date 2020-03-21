class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.moves = 0

    def distributeCoins(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.moves

    def dfs(self, node: TreeNode) -> int:
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.moves += abs(left) + abs(right)
        return node.val + left + right - 1


if __name__ == '__main__':
    pass
