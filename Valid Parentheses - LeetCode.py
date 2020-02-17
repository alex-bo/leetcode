class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('{', '(', '['):
                stack.append(c)
            elif stack and (
                    (c == ')' and stack[-1] == '(') or
                    (c == ']' and stack[-1] == '[') or
                    (c == '}' and stack[-1] == '{')
            ):
                stack.pop()
            else:
                return False
        return not bool(stack)


def test_one(s: str, expected: bool):
    print(s)
    actual = Solution().isValid(s)
    if expected == actual:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


if __name__ == '__main__':
    test_one('(){}[]', True)
    test_one('(', False)
