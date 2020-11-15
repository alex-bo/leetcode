class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # desiredTotal is unreachable with given maxChoosableInteger
        if desiredTotal > (maxChoosableInteger * (maxChoosableInteger + 1) // 2):
            return False
        # already reached the goal of 0 total
        if desiredTotal <= 0:
            return True
        return recursive_solution([i+1 for i in range(maxChoosableInteger)], desiredTotal, {})


def recursive_solution(choosableIntegers: list, desiredTotal: int, cache: dict) -> bool:
    if not choosableIntegers:
        return False
    tpl = tuple(choosableIntegers)
    if tpl in cache:
        return cache[tpl]
    if choosableIntegers[-1] >= desiredTotal:
        cache[tpl] = True
        return True
    for i, n in enumerate(choosableIntegers):
        if not recursive_solution(choosableIntegers[:i] + choosableIntegers[i+1:], desiredTotal - n, cache):
            cache[tpl] = True
            return True
    cache[tpl] = False
    return False


if __name__ == '__main__':
    print(10, 0, Solution().canIWin(10, 0))
    print(10, 11, Solution().canIWin(10, 11))
