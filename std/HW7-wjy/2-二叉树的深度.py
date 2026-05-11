def tree_depth(node, children):
    if node == -1:
        return 0
    left, right = children[node]
    return max(tree_depth(left, children), tree_depth(right, children)) + 1

n = int(input())
children = [(0,0) for _ in range(n+1)]
for i in range(1, n + 1):
    left, right = map(int, input().split())
    children[i] = (left, right)
depth = tree_depth(1, children)
print(depth)