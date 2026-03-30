import collections
t = int(input())
for _ in range(t):
    n = int(input())
    stack = []
    queue = collections.deque()
    is_stack = True
    for _ in range(n):
        type, val = tuple(map(int, input().split()))
        if type == 1:
            stack.append(val)
            queue.append(val)
        elif type == 2:
            s = stack.pop()
            q = queue.popleft()
            if s != q:
                if val == q:
                    is_stack = False
    if is_stack:
        print("Stack")
    else:
        print("Queue")