t = int(input())
for _ in range(t):
    n = int(input())
    stores = list(map(int, input().split()))
    dp = [0 for _ in range(n)]
    dp[n-1] = stores[n-1]
    dp[n-2] = max(stores[n-1], stores[n-2])
    for i in range(n-3, -1, -1):
        dp[i] = max(stores[i] + dp[i+2], dp[i+1])
    print(dp[0])