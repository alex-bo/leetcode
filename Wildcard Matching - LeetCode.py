
class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        return match(s, p, 0, 0)


def match(s: str, p: str, si: int, pi: int) -> bool:
    # end of s
    if len(s) <= si:
        # end of p or only *'s left
        if len(p) <= pi or len(p[pi:].replace('*', '')) == 0:
            return True
        return False

    # end of p
    if len(p) <= pi:
        return False

    # *
    if p[pi] == '*':
        if match(s, p, si+1, pi):
            return True
        if match(s, p, si+1, pi+1):
            return True
        if match(s, p, si, pi+1):
            return True
        return False

    # ?
    if p[pi] == '?':
        return match(s, p, si+1, pi+1)

    # character
    if s[si] == p[pi]:
        return match(s, p, si+1, pi+1)
    return False


def test_one(s: str, p: str, expected: bool):
    print(s)
    print(p)
    actual = Solution().isMatch(s, p)
    if actual == expected:
        print('OK')
    else:
        print('WRONG!')


def test():
    test_one('cb', '?a', False)
    test_one('aa', '*', True)
    test_one('aa', 'a', False)
    test_one('adceb', 'a*b', True)
    test_one('acdcb', 'a*c?b', False)
    test_one('adceb', '*a*b', True)
    test_one('aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab', '*ab***ba**b*b*aaab*b', True)


if __name__ == '__main__':
    # pass
    test()
