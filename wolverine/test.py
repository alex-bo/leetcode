import random
from time import time
from typing import List, Tuple

from structures.red_black_bst import RedBlackBST


def login_not_optimized(nums_count: int, values: List[Tuple[int, int, int]]) -> int:
    numbers = [0 for _ in range(nums_count)]
    max_value = 0
    for a, b, k in values:
        max_value = max(perform_operation(numbers, a, b, k), max_value)
    return max_value


def perform_operation(numbers, a, b, k):
    max_value = 0
    for i in range(a - 1, b):
        numbers[i] += k
        max_value = max(numbers[i], max_value)
    return max_value


def login_optimized(nums_count: int, values: List[Tuple[int, int, int]]) -> int:
    tree = RedBlackBST()
    max_value = 0
    for a, b, k in values:
        tree[a] = tree.get(a, default=0)
        tree[b] = tree.get(b, default=0)
        for key in tree.keys(a, b):
            v = tree[key]
            v += k
            tree[key] = v
            max_value = max(v, max_value)
    return max_value


def test_one(nums_count: int, values: List[Tuple[int, int, int]]):
    print('nums_count =', nums_count)
    print('len(values) =', len(values))
    start = time()
    res1 = login_not_optimized(nums_count, values)
    end = time()
    print('Not optimized done in {} seconds.'.format(round(end - start, 2)))
    start = time()
    res2 = login_optimized(nums_count, values)
    end = time()
    print('Optimized done in {} seconds.'.format(round(end - start, 2)))
    if res1 == res2:
        print('OK. res =', res1)
    else:
        print('WRONG! Optimized result {}, not optimized is {}.'.format(res2, res1))


def main():
    nums_count = random.randint(4000, 4000)
    values = []
    for _ in range(random.randint(4000, 4000)):
        a = 10  # random.randint(1, nums_count // 2)
        b = a + 1000
        values.append((a, b, random.randint(1, 10)))
    test_one(nums_count, values)


if __name__ == '__main__':
    main()
