stone_str = input()
original_str = input()

if len(stone_str) != len(original_str):
    print("NO")

else:
    count1 = [0] * 26
    for char in stone_str:
        count1[ord(char) - ord('A')] += 1
    count2 = [0] * 26
    for char in original_str:
        count2[ord(char) - ord('A')] += 1

    count1.sort()
    count2.sort()

    if count1 == count2:
        print("YES")
    else:
        print("NO")