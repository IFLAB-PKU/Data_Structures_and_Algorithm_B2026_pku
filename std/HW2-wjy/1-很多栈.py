n = int(input())

stacks = [[] for _ in range(100)]

for _ in range(n):
    operation = list(map(int, input().split()))
    if operation[0] == 1:
        x = operation[1] - 1
        y = operation[2]
        stacks[x].append(y)

    elif operation[0] == 2:
        x = operation[1] - 1
        if stacks[x] == []:
            print("-1")
            continue
        print(stacks[x].pop())
    
    else:
        x = operation[1] - 1
        y = operation[2] - 1
        if stacks[x] == []:
            print("-1")
            continue
        z = stacks[x].pop()
        print(z)
        stacks[y].append(z)