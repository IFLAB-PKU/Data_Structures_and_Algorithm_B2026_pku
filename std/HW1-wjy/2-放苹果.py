def method_num(apple_num, plate_num):
    if apple_num == 0:
        return 1
    if plate_num == 1:
        return 1
    if apple_num < plate_num:
        return method_num(apple_num, apple_num)
    return method_num(apple_num-plate_num, plate_num) + method_num(apple_num, plate_num-1)

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    print(method_num(m, n))
