class Solution:

    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        for i, (s, g) in enumerate(zip(secret, guess)):
            if s == g:
                guess = guess[:i - bulls] + guess[i - bulls + 1:]
                secret = secret[:i - bulls] + secret[i - bulls + 1:]
                bulls += 1
        cows = 0
        for g in guess:
            if g in secret:
                i = secret.index(g)
                secret = secret[:i] + secret[i + 1:]
                cows += 1
        return '{}A{}B'.format(bulls, cows)


def test():
    test_one('1807', '7810', '1A3B')
    test_one('1123', '0111', '1A1B')
    test_one('11', '11', '2A0B')


def test_one(secret: str, guess: str, expected: str):
    print(secret)
    print(guess)
    actual = Solution().getHint(secret, guess)
    if actual == expected:
        print('OK')
        return True
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))
        return False


if __name__ == '__main__':
    test()
