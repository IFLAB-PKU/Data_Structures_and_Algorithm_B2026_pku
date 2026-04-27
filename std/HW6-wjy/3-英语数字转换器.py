val = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90
}

while True:
    line = input()
    if not line:
        break

    words = line.split()
    total = 0
    temp = 0
    sign = 1
    
    for word in words:
        if word == "negative":
            sign = -1
        elif word == "million":
            total += temp * 1000000
            temp = 0
        elif word == "thousand":
            total += temp * 1000
            temp = 0
        elif word == "hundred":
            temp *= 100
        else:
            temp += val[word]
    
    total += temp
    print(total * sign)