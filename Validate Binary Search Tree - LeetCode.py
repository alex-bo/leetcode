# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return is_valid(root, None, None)


def is_valid(node: TreeNode, prev_left: TreeNode, prev_right: TreeNode) -> bool:
    if not node:
        return True

    if prev_left and prev_left.val >= node.val:
        return False
    if prev_right and prev_right.val <= node.val:
        return False

    if not is_valid(node.left, prev_left, node):
        return False
    if not is_valid(node.right, node, prev_right):
        return False

    return True
