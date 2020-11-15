class Solution:
    def divisorGame(self, N: int) -> bool:
        return solve(N, {})


def solve(N: int, cache: dict) -> bool:
    if N <= 1:
        return False
    if N in cache:
        return cache[N]
    for i in range(1, N // 2 + 1):
        if (N % i) == 0:
            if not solve(N - i, cache):
                # Bob cannot take a move
                cache[N] = True
                return True
    # Alice cannot take a move
    cache[N] = False
    return False


if __name__ == '__main__':
    print(Solution().divisorGame(100))
