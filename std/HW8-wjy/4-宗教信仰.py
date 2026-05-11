def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, rank, x, y):
    rx = find(parent, x)
    ry = find(parent, y)
    if rx == ry:
        return
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    elif rank[rx] > rank[ry]:
        parent[ry] = rx
    else:
        parent[ry] = rx
        rank[rx] += 1

case_no = 0
while True:
    case_no += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    for _ in range(m):
        i, j = map(int, input().split())
        union(parent, rank, i, j)
    
    cnt = sum(1 for i in range(1, n + 1) if parent[i] == i)
    print(f"Case {case_no}: {cnt}")