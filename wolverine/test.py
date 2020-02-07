# Enter your code here. Read input from STDIN. Print output to STDOUT


def main():
    N, M = [int(n) for n in input().split(' ')]
    numbers = [0 for _ in range(N)]
    max_value = 0
    for i in range(M):
        a, b, k = [int(n) for n in input().split(' ')]
        max_value = max(perform_operation(numbers, a, b, k), max_value)
    print(max_value)


def perform_operation(numbers, a, b, k):
    max_value = 0
    for i in range(a - 1, b):
        numbers[i] += k
        max_value = max(numbers[i], max_value)
    return max_value


if __name__ == '__main__':
    main()
