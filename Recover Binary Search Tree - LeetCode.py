# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.node1 = None
        self.node2 = None
        self.prev = None

    def recoverTree(self, root: TreeNode) -> None:
        self.traverse(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val

    def traverse(self, node: TreeNode) -> None:
        if not node:
            return

        self.traverse(node.left)

        if self.prev and self.prev.val > node.val:
            if self.node1 is None:
                self.node1 = self.prev
            self.node2 = node
        self.prev = node

        self.traverse(node.right)


def solution_with_aux_list(root: TreeNode) -> None:
    nodes = []
    add_nodes(root, nodes)
    if len(nodes) < 2:
        return

    node1, node2 = None, None
    for i, node in enumerate(nodes):
        if i == 0:
            if node.val > nodes[i + 1].val:
                node1 = node
        elif i == len(nodes) - 1:
            if node.val < nodes[i - 1].val:
                node2 = node
        elif node1 is None:
            if node.val > nodes[i + 1].val:
                node1 = node
        else:
            if node.val < nodes[i - 1].val:
                node2 = node
    node1.val, node2.val = node2.val, node1.val


def add_nodes(node: TreeNode, nodes: list) -> None:
    if not node:
        return

    add_nodes(node.left, nodes)
    nodes.append(node)
    add_nodes(node.right, nodes)


if __name__ == '__main__':
    Solution().recoverTree(
        TreeNode(
            val=3,
            left=TreeNode(val=1),
            right=TreeNode(
                val=4,
                left=TreeNode(val=2)
            )
        )
    )
