import heapq

n = int(input())
heap = []
for _ in range(n):
    op = list(map(int, input().split()))
    if op[0] == 1:
        u = op[1]
        heapq.heappush(heap, u)
    elif op[0] == 2:
        val = heapq.heappop(heap)
        print(str(val))