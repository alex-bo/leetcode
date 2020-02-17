from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = []
        lines = [line]
        line_size = 0
        for word in words:
            word_size = len(word)
            if line:
                word_size += 1
            if (line_size + word_size) > maxWidth:
                line = []
                lines.append(line)
                line_size = 0
                word_size = len(word)  # new line (no space needed)
            line.append(word)
            line_size += word_size
        return [
            justify_line(line, maxWidth, i == len(lines) - 1)
            for i, line in enumerate(lines)
        ]


def justify_line(line: List[str], width: int, last_line: bool) -> str:
    if len(line) <= 1 or last_line:
        ln = ' '.join(line)
        return ln + ' ' * (width - len(ln))
    spaces_count = width - sum(len(word) for word in line)
    spaces_per_word = spaces_count // (len(line) - 1)
    res = [line[0]]
    for w in line[1:]:
        if spaces_count > 0:
            res.append(' ' * min(spaces_per_word, spaces_count))
            spaces_count -= len(res[-1])
        res.append(w)
    for i in range(spaces_count):
        word_index = (i % (len(line) - 1) + 1) * 2
        res[word_index] = ' ' + res[word_index]
    return ''.join(res)


def test_one(words: List[str], maxWidth: int, expected: List[str]):
    print(words)
    print(maxWidth)
    actual = Solution().fullJustify(words, maxWidth)
    if actual == expected:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


if __name__ == '__main__':
    test_one(["This", "is", "an", "example", "of", "text", "justification."], 16,
             ["This    is    an", "example  of text", "justification.  "])
    test_one(["What", "must", "be", "acknowledgment", "shall", "be"], 16,
             ["What   must   be", "acknowledgment  ", "shall be        "])
    test_one(
        ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
         "is", "everything", "else", "we", "do"]
        , 20,
        ["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is",
         "everything  else  we", "do                  "])
