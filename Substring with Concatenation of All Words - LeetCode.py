from typing import List

from structures.trie import TernarySearchTrie


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not words:
            return []

        # construct words dict
        words_dict = TernarySearchTrie()
        for w in words:
            words_dict[w] = words_dict.get(w, 0) + 1

        word_len = len(words[0])
        result = []
        pos = 0
        while pos < len(s):
            if find_next_word(s, pos, words_dict, word_len):
                result.append(pos)
            pos += 1

        return result


def find_next_word(s: str, pos: int, words: TernarySearchTrie, word_len: int) -> bool:

    # all words found on previous step
    if not words:
        return True

    # reached end of s but still have words
    if pos >= len(s):
        return False

    next_word = s[pos:pos + word_len]

    if next_word in words:
        words[next_word] -= 1
        if words[next_word] <= 0:
            del words[next_word]
        res = find_next_word(s, pos + word_len, words, word_len)
        words[next_word] = words.get(next_word, 0) + 1
        return res

    # next word not found
    return False


def test_one(s: str, words: List[str], expected: List[int]):
    print(s)
    print(words)
    actual = Solution().findSubstring(s, words)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


def test():
    test_one('barfoothefoobarman', ['foo', 'bar'], [0, 9])
    test_one('barfoofoobarthefoobarman', ['foo', 'bar', 'the'], [6,9,12])


if __name__ == '__main__':
    test()
