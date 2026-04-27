dictionary = {}
while True:
    parts = input().split()
    if len(parts) == 2:
        eng, foreign = parts
        dictionary[foreign] = eng
    else:
        break

try:
    while True:
        line = input()
        print(dictionary.get(line, "eh"))

except EOFError:
    pass