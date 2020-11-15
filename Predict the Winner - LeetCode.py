from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        cache = {}
        res = recursive_solution(nums, 0, 0, cache, True)
        return res


def recursive_solution(nums: List[int], curr_sum: int, other_sum: int, cache: dict, first_player_move: bool) -> bool:
    if not nums:
        return curr_sum >= other_sum if first_player_move else curr_sum > other_sum
    tpl = (tuple(nums), curr_sum, other_sum, first_player_move)
    if tpl in cache:
        return cache[tpl]

    n = nums.pop(0)
    try:
        if not recursive_solution(nums, other_sum, curr_sum + n, cache, not first_player_move):
            cache[tpl] = True
            return True
    finally:
        nums.insert(0, n)

    if len(nums) > 1:
        n = nums.pop(-1)
        try:
            if not recursive_solution(nums, other_sum, curr_sum + n, cache, not first_player_move):
                cache[tpl] = True
                return True
        finally:
            nums.append(n)

    cache[tpl] = False
    return False


if __name__ == '__main__':
    print([1, 5, 2], Solution().PredictTheWinner([1, 5, 2]))
    print([0], Solution().PredictTheWinner([0]))
    print([1, 2, 99], Solution().PredictTheWinner([1, 2, 99]))
    print([2, 99], Solution().PredictTheWinner([2, 99]))
