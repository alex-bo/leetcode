#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#
from collections import namedtuple

LogEntry = namedtuple('LogEntry', ['sender', 'recipient', 'amount'])


def processLogs(logs, threshold):
    log_entries = [parse_one(l) for l in logs]
    counts = {}
    for log in log_entries:
        counts[log.sender] = counts.get(log.sender, 0) + 1
        if log.sender != log.recipient:
            counts[log.recipient] = counts.get(log.recipient, 0) + 1

    res = []
    for user, cnt in counts.items():
        if cnt >= threshold:
            res.append(user)
    return [str(u) for u in sorted(res)]


def parse_one(log: str) -> LogEntry:
    s, r, a = log.split(' ')
    return LogEntry(int(s), int(r), int(a))


if __name__ == '__main__':
    pass
