def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

try:
    while True:
        n, m = map(int, input().split())
        parent = list(range(n+1))
        for _ in range(m):
            x, y = map(int, input().split())
            rx = find(parent, x)
            ry = find(parent, y)
            if rx == ry:
                print("Yes")
            else:
                print("No")
                parent[ry] = rx

        roots = [str(i) for i in range(1, n + 1) if parent[i] == i]
        print(len(roots))
        print(" ".join(roots))

except EOFError:
    pass