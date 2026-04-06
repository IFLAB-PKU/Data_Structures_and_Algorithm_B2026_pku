n = int(input())
odds = [i for i in range(1, n + 1, 2)]
solutions = []

def dfs(start, cur_sum, path):
    if cur_sum == n:
        solutions.append(path[:])
        return
    for i in range(start, len(odds)):
        num = odds[i]
        if cur_sum + num > n:
            break
        path.append(num)
        dfs(i + 1, cur_sum + num, path)
        path.pop()

dfs(0, 0, [])

for sol in solutions:
    print(' '.join(map(str, sol)))
print(len(solutions))