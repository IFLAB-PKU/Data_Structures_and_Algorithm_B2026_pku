s = input()

children = []
depth = []
children.append([])
depth.append(0)
stack = [0]
max_h1 = 0
node_cnt = 1

for ch in s:
    if ch == 'd':
        parent = stack[-1]
        node_id = node_cnt
        node_cnt += 1
        children.append([])
        children[parent].append(node_id)
        d = depth[parent] + 1
        depth.append(d)
        if d > max_h1:
            max_h1 = d
        stack.append(node_id)
    elif ch == 'u':
        stack.pop()

n = node_cnt

left = [-1] * n
right = [-1] * n
for u in range(n):
    childs = children[u]
    if childs:
        left[u] = childs[0]
        for i in range(len(childs) - 1):
            right[childs[i]] = childs[i + 1]

max_h2 = 0
stack_dfs = [(0, 0)]
while stack_dfs:
    node, dep = stack_dfs.pop()
    if dep > max_h2:
        max_h2 = dep
    l = left[node]
    r = right[node]
    if l != -1:
        stack_dfs.append((l, dep + 1))
    if r != -1:
        stack_dfs.append((r, dep + 1))

print(f"{max_h1} => {max_h2}")