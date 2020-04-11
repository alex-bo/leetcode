from typing import List


class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in rooms]
        to_visit = [k for k in rooms[0]]
        visited[0] = True

        while to_visit:
            k = to_visit.pop()
            if not visited[k]:
                visited[k] = True
                to_visit.extend(rooms[k])
        return all(visited)
