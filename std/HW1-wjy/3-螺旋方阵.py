n, m = map(int, input().split())
square = [[0 for _ in range(n)] for _ in range(n)]
line = 0
col = 0
direction = 0
update = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i in range(1, m):
    square[line][col] = i

    line_t = line + update[direction][0]
    col_t = col + update[direction][1]
    if line_t == -1 or line_t == n or col_t == -1 or col_t == n or square[line_t][col_t] != 0:
        direction = (direction + 1) % 4

    line += update[direction][0]
    col += update[direction][1]

print(line+1, col+1)