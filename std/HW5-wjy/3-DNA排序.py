def count_pair(dna):
    num_c = 0
    num_g = 0
    num_t = 0
    count = 0
    for ch in dna:
        if ch == 'A':
            count += num_c + num_g + num_t
        elif ch == 'C':
            count += num_g + num_t
            num_c += 1
        elif ch == 'G':
            count += num_t
            num_g += 1
        elif ch == 'T':
            num_t += 1
    return count

n, m = list(map(int, input().split()))
dnas = [input() for _ in range(m)]

sorted_dnas = sorted(dnas, key=count_pair)
for dna in sorted_dnas:
    print(dna)