t = int(input())
def floor(n, cache):
    if n in cache:
        return cache[n]
    res_n = floor(n-1, cache) + floor(n-2, cache)
    cache[n] = res_n
    return res_n

cache = {1:1, 2:2, 0:0}

for _ in range(t):
    n = int(input())
    print(floor(n, cache))