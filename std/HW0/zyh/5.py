from collections import defaultdict, deque, Counter

# from functools import cache
# from sortedcontainers import SortedSet, SortedDict, SortedList
from typing import List, Tuple, Set
from math import inf
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
import math
import sys

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())


def solve():
    n = float(input())
    res = 0
    if 0 <= n < 5:
        res = -n + 2.5
    elif 5 <= n < 10:
        res = 2 - 1.5 * (n - 3) ** 2
    else:
        res = n / 2 - 1.5
    print(f"{res:.3f}")
    return


solve()