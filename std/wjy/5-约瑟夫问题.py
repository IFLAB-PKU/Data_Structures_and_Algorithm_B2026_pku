while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    monkeys = [i + 1 for i in range(n)]
    p = 0
    len = n
    for i in range(n-1):
        for j in range(m - 1):
            p = (p + 1) % len
        
        monkeys.remove(monkeys[p])
        len -= 1
    
    print(monkeys[0])
