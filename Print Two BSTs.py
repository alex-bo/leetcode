from binarytree import Node, bst

"""
Return/print two BSTs in sorted order.
Restrictions: use it in-place.
Example:

tree1:
    __6
   /
  4
 / \
2   5


tree2:
  1__
 /   \
0     3
     / \
    2   5

result:
    [0, 1, 2, 2, 3, 4, 5, 5, 6]

"""


def print_trees(tree1: Node, tree2: Node) -> list:
    stack1 = []
    stack2 = []
    result = []
    put_left_nodes_to_stack(stack1, tree1)
    put_left_nodes_to_stack(stack2, tree2)

    while True:
        node = None
        stack = None
        if stack1 and stack2:
            if stack1[-1].value <= stack2[-1].value:
                node = stack1.pop()
                stack = stack1
            else:
                node = stack2.pop()
                stack = stack2
        elif stack1:
            node = stack1.pop()
            stack = stack1
        elif stack2:
            node = stack2.pop()
            stack = stack2

        if node:
            put_left_nodes_to_stack(stack, node.right)
            result.append(node.value)
        else:
            break

    return result


def put_left_nodes_to_stack(stack: list, tree: Node):
    if not tree:
        return
    stack.append(tree)
    put_left_nodes_to_stack(stack, tree.left)


def main():
    tree1 = bst(height=2, is_perfect=False)
    tree2 = bst(height=2, is_perfect=False)
    print('-----------------------------------------------------')
    print('tree1 {}:'.format(len(tree1)))
    print(tree1)
    print('tree2 {}:'.format(len(tree2)))
    print(tree2)
    res = print_trees(tree1, tree2)
    print('{} {}'.format(len(res), res))
    if len(res) != len(tree1) + len(tree2):
        raise Exception('Incorrect!')
    for i, v in enumerate(res):
        if i > 0:
            if res[i-1] > res[i]:
                raise Exception('Incorrect!')


if __name__ == '__main__':
    for _ in range(10):
        main()
