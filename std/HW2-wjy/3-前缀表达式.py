add = '+'
sub = '-'
mul = '*'
div = '/'
op = [add, sub, mul, div]
num_stack = []

expr = input()
for ch in reversed(expr):
    if ch in op:
        a = num_stack.pop()
        b = num_stack.pop()
        res = 0
        if ch == add:
            res = a + b
        elif ch == sub:
            res = a - b
        elif ch == mul:
            res = a * b
        else:
            res = a // b
        
        num_stack.append(res)
        
    else:
        num = int(ch)
        num_stack.append(num)

print(num_stack[-1])