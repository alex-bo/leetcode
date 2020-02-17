from time import time


def split_by_spaces(in_str: str) -> list:
    res = []
    curr_word = []
    quote_open = False
    for c in in_str:
        if c == '"':
            quote_open = not quote_open
        elif c == ' ' and not quote_open:
            res.append(''.join(curr_word))
            curr_word = []
        else:
            curr_word.append(c)
    if curr_word:
        res.append(''.join(curr_word))
    return res


def test_one(in_str: str, expected: list):
    print(in_str)
    print(expected)
    actual = split_by_spaces(in_str)
    if expected == actual:
        print('OK')
    else:
        print('WRONG! Got {}, expected {}.'.format(actual, expected))


def test():
    test_one('the quick brown "fox jumped"', ["the", "quick", "brown", "fox jumped"])


def generate_file(file_path: str, txt: str, sz: int):
    start = time()
    written = 0
    with open(file_path, 'w') as f:
        while written < sz:
            f.write(txt)
            written += len(txt)
    print('{} bytes written to {} in {} sec.'.format(written, file_path, round(time() - start, 2)))


def main():
    file_path = r'C:\tmp\test.txt'
    # generate_file(file_path, 'the quick brown "fox jumped" ', 2**25)
    with open(file_path) as f:
        txt = f.read()
    start = time()
    split_by_spaces(txt)
    print('{} sec to process.'.format(round(time() - start, 2)))


if __name__ == '__main__':
    # test()
    main()

