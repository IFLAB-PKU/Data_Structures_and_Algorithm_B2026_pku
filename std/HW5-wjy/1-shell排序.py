n = int(input())
arr = list(map(int, input().split()))
increments = []
k = 1
while True:
    h = (1 << k) - 1  # 2^k - 1
    if h < n:
        increments.append(h)
        k += 1
    else:
        break

for gap in reversed(increments):
    for i in range(gap, n):
        temp = arr[i]
        j = i
        while j >= gap and arr[j - gap] > temp:
            arr[j] = arr[j - gap]
            j -= gap
        arr[j] = temp

    print(" ".join(map(str, arr)))
