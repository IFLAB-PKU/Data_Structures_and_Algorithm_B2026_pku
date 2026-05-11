import heapq

def min_wpl(weights):
    heapq.heapify(weights)
    total_wpl = 0
    while len(weights) > 1:
        a = heapq.heappop(weights)
        b = heapq.heappop(weights)
        cost = a + b
        total_wpl += cost
        heapq.heappush(weights, cost)
    return total_wpl

n = int(input())
weights = list(map(int, input().split()))
print(min_wpl(weights))