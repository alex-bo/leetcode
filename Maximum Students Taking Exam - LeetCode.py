from functools import lru_cache
from typing import List, Set
from collections import namedtuple

Seat = namedtuple('Seat', ['m', 'n'])


class Solution:

    def maxStudents(self, seats: List[List[str]]) -> int:
        pass


@lru_cache()
def place_seat(not_used_seats: Set[Seat], used_seats: Set[Seat]) -> int:
    pass
