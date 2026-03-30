import collections

n = int(input())
cards = input().split()

queues = [collections.deque() for _ in range(9)]

for card in cards:
    queues[int(card[1])-1].append(card)

queue_res = [[] for _ in range(9)]
sort_res = []

for i in range(9):
    print(f"Queue{i+1}:", end="")
    queue = queues[i]
    while queue:
        card = queue.popleft()
        queue_res[i].append(card)
        sort_res.append(card)
    print(*queue_res[i])

for card in sort_res:
    queues[ord(card[0])-ord("A")].append(card)

queue_res.clear()
queue_res = [[] for _ in range(4)]
sort_res.clear()

for i in range(4):
    print(f"Queue{chr(i+ord('A'))}:", end="")
    queue = queues[i]
    while queue:
        card = queue.popleft()
        queue_res[i].append(card)
        sort_res.append(card)
    print(*queue_res[i])

print(*sort_res)