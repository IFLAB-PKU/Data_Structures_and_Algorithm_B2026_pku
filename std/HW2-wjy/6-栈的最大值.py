n = int(input())
stack = []
max_stack = []
for _ in range(n):
    op = list(map(int, input().split()))
    if op[0] == 1:
        num = op[1]
        stack.append(num)
        if max_stack == [] or num >= max_stack[-1]:
            max_stack.append(num)
    
    elif op[0] == 2:
        if stack == []:
            continue
        num = stack.pop()
        if num == max_stack[-1]:
            max_stack.pop()

    else:
        if stack == []:
            print("0")
        else:
            print(max_stack[-1])