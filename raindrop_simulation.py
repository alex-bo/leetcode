import random

from structures.red_black_bst import RedBlackBST


class Node:

    def __init__(self, is_left: bool):
        self.is_left = is_left


def simulate(platform_length: float, drop_radius: float) -> int:
    """
    Given a platform of length L (double) and raindrop splash radius R (double), simulate random rain
    and calculate how many drops need to fall to cover entire surface.
    """
    bst = RedBlackBST()
    bst[0.0] = Node(True)
    bst[platform_length] = Node(False)
    drops_count = 0

    while bst:
        drop = random.random() * platform_length
        left_bound = drop - drop_radius
        right_bound = drop + drop_radius
        drops_count += 1

        # delete internal nodes
        for key in list(bst.keys(left_bound, right_bound)):
            del bst[key]

        if not bst:
            break

        # check left node
        if left_bound >= bst.min():
            left_node = bst[bst.floor(left_bound)]
            if left_node.is_left:
                bst[left_bound] = Node(False)

        # check right node
        if right_bound <= bst.max():
            right_node = bst[bst.ceiling(right_bound)]
            if not right_node.is_left:
                bst[right_bound] = Node(True)

    return drops_count


def main():
    values = [
        (10.0, 10.0),
        (100.0, 10.0),
        (1000.0, 10.0),
        (10000.0, 10.0),
    ]
    for platform_length, radius in values:
        print()
        print('simulating...')
        print('platform_length = {}'.format(platform_length))
        print('radius = {}'.format(radius))
        drops_count = simulate(platform_length, radius)
        print('drops_count = {}'.format(drops_count))


if __name__ == '__main__':
    main()


