import random
from collections import Counter


def get_probability_index(probabilities: list) -> int:
    r = random.random()
    curr_prob = 0
    for i, n in enumerate(probabilities):
        curr_prob += n
        if r < curr_prob:
            return i
    return i


def main():
    probabilities = [.1, .2, .3, .4, .1]
    print(probabilities)
    print(Counter(get_probability_index(probabilities) for _ in range(1000)))
    print(Counter(get_probability_index(probabilities) for _ in range(10000)))
    print(Counter(get_probability_index(probabilities) for _ in range(100000)))


if __name__ == '__main__':
    main()
