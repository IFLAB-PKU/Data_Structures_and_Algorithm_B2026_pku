brackets = input()
left_brackets = []
bracket_dic = {'(':')', '[':']', '{':'}'}
judge = True
for bracket in brackets:
    if bracket in bracket_dic.keys():
        left_brackets.append(bracket)
    else:
        if left_brackets == []:
            judge = False
            break

        left = left_brackets.pop()
        if bracket_dic[left] != bracket:
            judge = False
            break

if judge:
    print("Yes")
else:
    print("No")
