class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1] + ord(s2[j-1])
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + ord(s1[i-1])
                else:
                    dp[i][j] = min(

                        # up
                        dp[i-1][j] + ord(s1[i-1]),

                        # left
                        dp[i][j-1] + ord(s2[j-1]),

                        # diagonal
                        dp[i-1][j-1] + (0 if s1[i-1] == s2[j-1] else ord(s1[i-1]) + ord(s2[j-1]))
                    )

        return dp[-1][-1]


if __name__ == '__main__':
    print(231, Solution().minimumDeleteSum('sea', 'tea'))
    print(403, Solution().minimumDeleteSum('delete', 'leet'))
