from typing import List, Tuple


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return top_down_solution(days, list(zip(costs, [1, 7, 30])), len(days) - 1, {})


def bottom_up_solution(days: List[int], costs: List[int]) -> int:
    dp = [2 ** 32] * (days[-1] + 1)
    pass_days = [1, 7, 30]
    dp[0] = 0
    visit_days = set(days)
    for i in range(1, len(dp)):
        if i not in visit_days:  # no visit on this day
            dp[i] = dp[i - 1]
            continue
        for cost, ticket_days in zip(costs, pass_days):
            dp[i] = min(
                dp[i],
                cost + (dp[i - ticket_days] if ticket_days <= i else 0)
            )
    return dp[-1]


def top_down_solution(days: List[int], costs: List[Tuple[int, int]], day_index: int, cache: dict) -> int:
    if day_index not in cache:
        if day_index == 0:
            return min(c[0] for c in costs)
        if day_index < 0:
            return 0
        res = 2 ** 32
        for cost, ticket_days in costs:
            res = min(
                res,
                top_down_solution(days, costs, find_next_day(days, day_index, ticket_days), cache) + cost
            )
        cache[day_index] = res
    return cache[day_index]


def find_next_day(days: List[int], day_index: int, ticket_days: int) -> int:
    for next_day_index in reversed(range(0, day_index)):
        if days[next_day_index] <= (days[day_index] - ticket_days):
            return next_day_index
    return -1


if __name__ == '__main__':
    actual = Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15])
    print(actual, 11)
    actual = Solution().mincostTickets(
        [6, 9, 10, 14, 15, 16, 17, 18, 20, 22, 23, 24, 29, 30, 31, 33, 35, 37, 38, 40, 41, 46, 47, 51, 54, 57, 59, 65,
         70, 76, 77, 81, 85, 87, 90, 91, 93, 94, 95, 97, 98, 100, 103, 104, 105, 106, 107, 111, 112, 113, 114, 116, 117,
         118, 120, 124, 128, 129, 135, 137, 139, 145, 146, 151, 152, 153, 157, 165, 166, 173, 174, 179, 181, 182, 185,
         187, 188, 190, 191, 192, 195, 196, 204, 205, 206, 208, 210, 214, 218, 219, 221, 225, 229, 231, 233, 235, 239,
         240, 245, 247, 249, 251, 252, 258, 261, 263, 268, 270, 273, 274, 275, 276, 280, 283, 285, 286, 288, 289, 290,
         291, 292, 293, 296, 298, 299, 301, 303, 307, 313, 314, 319, 323, 325, 327, 329, 334, 339, 340, 341, 342, 344,
         346, 349, 352, 354, 355, 356, 357, 358, 359, 363, 364]
        , [21, 115, 345])
    print(actual, 3040)
