
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_res = 0
        stack = [-1]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_res = max(max_res, i - stack[-1])
                else:
                    stack.append(i)
        return max_res


def test_one(s: str, expected: int):
    print(s)
    actual = Solution().longestValidParentheses(s)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


if __name__ == '__main__':
    test_one('(()', 2)
    test_one(')()())', 4)
    test_one('()(()', 2)
