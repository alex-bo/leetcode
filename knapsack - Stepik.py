from collections import namedtuple
from typing import List, Callable

from utils import print_execution_time

Item = namedtuple('Item', ['cost', 'weight'])


def with_repetitions(weight: int, items: List[Item]) -> int:
    """
    bottom-up
    """
    dp = [0 for _ in range(weight + 1)]
    for w in range(weight + 1):
        for item in items:
            if w < item.weight:
                continue
            dp[w] = max(dp[w], dp[w - item.weight] + item.cost)
    return dp[-1]


def with_repetitions_recursive(weight: int, items: List[Item], cache: dict) -> int:
    """
    top-down
    """
    if weight not in cache:
        max_value = 0
        for item in items:
            if item.weight <= weight:
                max_value = max(
                    max_value,
                    with_repetitions_recursive(weight - item.weight, items, cache) + item.cost
                )
        cache[weight] = max_value
    return cache[weight]


def without_repetitions(weight: int, items: List[Item]) -> int:
    """
    bottom_up
    """
    dp = [[0 for _ in range(len(items) + 1)] for _ in range(weight + 1)]
    for w in range(1, weight + 1):
        for i, item in enumerate(items):
            i += 1  # dp matrix is 1-based, first item has index 1, not 0
            dp[w][i] = dp[w][i - 1]  # optimal capacity w/o current item is default
            if w >= item.weight:
                dp[w][i] = max(
                    dp[w][i],
                    dp[w - item.weight][i - 1] + item.cost
                )
    return dp[-1][-1]


def without_repetitions_recursive(weight: int, items: List[Item], cache: dict) -> int:
    if weight not in cache:
        max_value = 0
        for i, item in enumerate(items):
            if item.weight <= weight:
                max_value = max(
                    max_value,
                    without_repetitions_recursive(
                        weight - item.weight,
                        items[:i] + items[i + 1:],  # exclude current element
                        cache
                    ) + item.cost
                )
        cache[weight] = max_value
    return cache[weight]


def test(func: Callable, expected: int, *args):
    weight = 5958
    items = [
        Item(30, 6),
        Item(14, 3),
        Item(16, 4),
        Item(9, 2),
    ]

    @print_execution_time(func.__name__)
    def do_things():
        print('expected: {}\tgot: {}'.format(expected, func(weight, items, *args)))

    do_things()


if __name__ == '__main__':
    test(with_repetitions, 48)
    test(with_repetitions_recursive, 48, {})
    test(without_repetitions, 46)
    test(without_repetitions_recursive, 46, {})
