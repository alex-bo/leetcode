

class Solution:

    def longestPalindrome(self, s: str) -> str:
        mx = ''
        for i in range(len(s)):
            mx = max(
                find_palindrome(s, i - 1, i),
                find_palindrome(s, i, i),
                mx,
                key=lambda ss: len(ss)
            )
        return mx


def find_palindrome(s: str, left: int, right: int) -> str:
    res = ''
    for j in range(len(s)):
        lft = left - j
        rgt = right + j
        if lft < 0 or rgt >= len(s) or s[lft] != s[rgt]:
            break
        res = s[lft:rgt + 1]
    return res


def test_one(s: int, expected: str):
    print(s)
    actual = Solution().longestPalindrome(s)
    if len(actual) == len(expected):
        print('OK')
    else:
        print('WRONG!')


def test():
    test_one('babad', 'bab')


if __name__ == '__main__':
    test()
