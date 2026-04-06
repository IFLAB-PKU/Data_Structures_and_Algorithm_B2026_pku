dir = [(1,0),(-1,0),(0,1),(0,-1)]

r, c = list(map(int, input().split()))
snow = []
dp = [[-1 for _ in range(c)] for _ in range(r)]

for i in range(r):
    snow.append(list(map(int, input().split())))

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    best = 1
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and snow[nx][ny] < snow[x][y]:
            best = max(best, dfs(nx, ny) + 1)
    dp[x][y] = best
    return best

ans = 0
for i in range(r):
    for j in range(c):
        ans = max(ans, dfs(i, j))

print(ans)