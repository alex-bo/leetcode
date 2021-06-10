def getBillionUsersDay(growthRates):
    # Write your code here
    days = 1
    lo = hi = 1
    while not try_days(growthRates, days):
        lo = days
        days *= 2
        hi = days
    while lo < hi:
        mid = (lo + hi) // 2
        if try_days(growthRates, mid):  # go down
            hi = mid
        else:  # go up
            lo = mid + 1
    return lo


def try_days(growthRates, days: int) -> bool:
    res = 0
    for rate in growthRates:
        if res >= 10 ** 9:
            return True
        res += rate ** days
    return res >= 10 ** 9


if __name__ == '__main__':
    print(79, getBillionUsersDay([1.1, 1.2, 1.3]))
