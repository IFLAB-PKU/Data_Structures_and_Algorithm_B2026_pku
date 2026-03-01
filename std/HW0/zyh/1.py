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
    n = input()
    for i in range(5):
        for j in range(abs(2 - i)):
            print(" ", end="")
        for j in range(5 - 2 * abs(2 - i)):
            print(n, end="")
        for j in range(abs(2 - i)):
            print(" ", end="")
        print()


solve()