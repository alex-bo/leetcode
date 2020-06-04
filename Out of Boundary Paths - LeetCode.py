

MAX_PATHS = 10**9 + 7

class Solution:

    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        return dp_solution(m, n, N, i, j)
        # return dfs(m, n, N, i, j, dict())


def dp_solution(m: int, n: int, N: int, i: int, j: int) -> int:
    dp1 = [[0 for _ in range(n)] for _ in range(m)]
    dp1[i][j] = 1
    count = 0
    dp2 = [[0 for _ in range(n)] for _ in range(m)]
    for move in range(N):
        for x in range(m):
            for y in range(n):
                if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                    count += dp1[x][y] * (
                        (1 if x == 0 else 0) +
                        (1 if x == (m - 1) else 0) +
                        (1 if y == 0 else 0) +
                        (1 if y == (n - 1) else 0)
                    )
                    count = count % MAX_PATHS
                dp2[x][y] = (
                    (dp1[x - 1][y] if x > 0 else 0) +
                    (dp1[x + 1][y] if x < (m - 1) else 0) +
                    (dp1[x][y - 1] if y > 0 else 0) +
                    (dp1[x][y + 1] if y < (n - 1) else 0)
                )
        dp1, dp2 = dp2, dp1
    return count


def dfs(m: int, n: int, N: int, i: int, j: int, memo: dict) -> int:
    if i < 0 or i >= m or j < 0 or j >= n:
        return 1
    if N <= 0:
        return 0
    coordinates = (i, j)
    if coordinates not in memo:
        memo[coordinates] = dict()
    if N not in memo[coordinates]:
        memo[coordinates][N] = (
            dfs(m, n, N - 1, i - 1, j, memo) +  # up
            dfs(m, n, N - 1, i + 1, j, memo) +  # down
            dfs(m, n, N - 1, i, j - 1, memo) +  # left
            dfs(m, n, N - 1, i, j + 1, memo)  # right
        ) % MAX_PATHS
    return memo[coordinates][N]


def test(m: int, n: int, N: int, i: int, j: int, expected: int):
    print(m, n)
    print(N)
    print(i, j)
    actual = Solution().findPaths(m, n, N, i, j)
    if expected == actual:
        print('OK')
    else:
        print('WRONG! Expected {}, got {}!'.format(expected, actual))


if __name__ == '__main__':
    test(2, 2, 2, 0, 0, 6)
    test(1, 3, 3, 0, 1, 12)
    test(1, 3, 4, 0, 1, 24)
    test(2, 3, 8, 1, 0, 1104)
    test(8, 50, 23, 5, 26, 914783380)

