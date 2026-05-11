def find(x, y):
    while x != y:
        if x > y:
            x //= 2
        else:
            y //= 2
    return x

t = int(input())
for _ in range(t):
    n = int(input())
    nodes = list(map(int, input().split()))
    ancestor = find(nodes[0], nodes[1])
    for i in range(2, n):
        ancestor = find(ancestor, nodes[i])
    print(ancestor)