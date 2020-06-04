

class Solution:

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        return dp_solution(N, K, r, c)


def dp_solution(N: int, K: int, r: int, c: int) -> float:
    dp1 = [[0.0 for _ in range(N)] for _ in range(N)]
    dp1[r][c] = 1.0
    for mv in range(K):
        dp2 = [[0.0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if dp1[i][j] == 0.0:
                    continue
                for i2, j2 in positions(N, i, j):
                    dp2[i2][j2] += dp1[i][j] / 8.0
        dp1, dp2 = dp2, dp1
    return sum(
        sum(i) for i in dp1
    )


def positions(N: int, r: int, c: int):
    for r2, c2 in (
            (r + 2, c + 1),
            (r - 2, c - 1),
            (r + 2, c - 1),
            (r - 2, c + 1),

            (r + 1, c + 2),
            (r - 1, c - 2),
            (r + 1, c - 2),
            (r - 1, c + 2),
    ):
        if 0 <= r2 < N and 0 <= c2 < N:
            yield r2, c2


def test(N: int, K: int, r: int, c: int, expected: float):
    print('N=' + str(N))
    print('K=' + str(K))
    print('r=' + str(r))
    print('r=' + str(r))
    print('c=' + str(c))
    actual = Solution().knightProbability(N, K, r, c)
    if expected == actual:
        print('OK')
    else:
        print('WRONG! Expected {}, got {}!'.format(expected, actual))


if __name__ == '__main__':
    test(3, 2, 0, 0, 0.0625)

