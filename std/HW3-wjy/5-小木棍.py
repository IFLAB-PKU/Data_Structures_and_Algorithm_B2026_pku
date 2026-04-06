def connecting_sticks(done_num, cur_stick_len, start, stick_len):
    if done_num == total // stick_len:
        return True
    if cur_stick_len == stick_len:
        # this stick is done
        return connecting_sticks(done_num + 1, 0, 0, stick_len)
    
    last_failed = -1
    for i in range(start, n):
        if not pieces_used[i] and pieces[i] != last_failed:
            if cur_stick_len + pieces[i] <= stick_len:
                pieces_used[i] = True # try connecting
                if connecting_sticks(done_num, cur_stick_len + pieces[i], i + 1, stick_len):
                    return True
                pieces_used[i] = False # failed
                last_failed = pieces[i]
                if cur_stick_len == 0 or cur_stick_len + pieces[i] == stick_len:
                    return False
    return False

while True:
    n = int(input())
    if n == 0:
        break

    pieces = list(map(int, input().split()))
    total = sum(pieces)
    pieces.sort(reverse=True)
    max_len = pieces[0]
    possible_lens = [i for i in range(max_len, total+1) if total % i == 0]

    for stick_len in possible_lens:
        pieces_used = [False for i in range(n)]
        if connecting_sticks(0, 0, 0, stick_len):
            print(stick_len)
            break
