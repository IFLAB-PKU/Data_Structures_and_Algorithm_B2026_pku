t, m = list(map(int, input().split()))
herbs = [[] for _ in range(m)]
for i in range(m):
    herbs[i] = list(map(int, input().split()))

dp = [0 for _ in range(t+1)]
for i in range(m):
    for j in range(t, -1, -1):
        time = herbs[i][0]
        value = herbs[i][1]
        if time <= j:
            dp[j] = max(dp[j], dp[j-time]+value)

print(dp[t])