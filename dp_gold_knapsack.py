# put your python code here
from functools import lru_cache


def solution(weight, items):
    dp = [[0 for _ in range(len(items) + 1)] for _ in range(weight + 1)]
    for w in range(1, weight + 1):
        for i, item_weight in enumerate(items):
            i += 1  # 1-based
            dp[w][i] = dp[w][i - 1]
            if item_weight <= w:
                dp[w][i] = max(
                    dp[w][i],
                    dp[w-item_weight][i-1] + item_weight
                )
    return dp[-1][-1]


def recursive_solution(weight, items, cache):
    if weight in cache:
        return cache[weight]
    max_value = 0
    for i in items:
        if i > weight:
            continue
        max_value = max(max_value, recursive_solution(weight - i, items, cache) + i)
    cache[weight] = max_value
    return max_value


if __name__ == '__main__':
    # weight = int(input().partition(' ')[0])
    # items = [int(i) for i in input().split(' ')]
    # print(solution(weight, items))
    print(solution(10, [1, 4, 8]))
    print(recursive_solution(10, [1, 4, 8], {}))


