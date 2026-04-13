n = int(input())
triangle = [[] for _ in range(n)]
for i in range(n):
    triangle[i] = list(map(int, input().split()))

dp = [0 for _ in range(n+1)]
for j in range(n):
    for i in range(j, n):
        dp[i-j+1] = triangle[i][j] + max(dp[i-j], dp[i-j+1])

print(max(dp))