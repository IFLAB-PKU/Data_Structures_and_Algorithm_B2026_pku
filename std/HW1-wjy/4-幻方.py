N = int(input())
n = N * 2 - 1
square = [[0 for _ in range(n)] for _ in range(n)]

line = 0
col = N - 1

for i in range(1, n**2+1):
    square[line][col] = i
    if line == 0 and col == n - 1:
        line += 1
        continue
    elif line == 0:
        line = n - 1
        col += 1
        continue
    elif col == n - 1:
        col = 0
        line -= 1
        continue
    elif square[line-1][col+1] != 0:
        line += 1
        continue
    else:
        line -= 1
        col += 1


for i in range(n):
    for j in range(n-1):
        print(square[i][j], end=" ")
    print(square[i][n-1])