from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False for _ in arr]
        visited[start] = True
        queue = deque([start], len(arr))
        while queue:
            i = queue.pop()
            if arr[i] == 0:
                return True
            left = i - arr[i]
            right = i + arr[i]
            if 0 <= left < len(arr) and not visited[left]:
                queue.appendleft(left)
                visited[left] = True
            if 0 <= right < len(arr) and not visited[right]:
                queue.appendleft(right)
                visited[right] = True
        return False


if __name__ == '__main__':
    print(True, Solution().canReach([4, 2, 3, 0, 3, 1, 2], 5))
