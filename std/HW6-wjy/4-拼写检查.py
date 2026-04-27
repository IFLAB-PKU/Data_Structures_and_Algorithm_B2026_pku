def is_similar(s1, s2):
    len1, len2 = len(s1), len(s2)
    
    if len1 == len2:
        diff_count = 0
        for i in range(len1):
            if s1[i] != s2[i]:
                diff_count += 1
            if diff_count > 1: 
                return False
        return diff_count == 1
    
    elif abs(len1 - len2) == 1:
        if len1 > len2:
            s1, s2 = s2, s1
            len1, len2 = len2, len1
        
        i = j = 0
        while i < len1 and j < len2:
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                j += 1
                if j - i > 1: 
                    return False
        return True

    return False

dictionary = []
while True:
    word = input()
    if word == "#":
        break
    
    dictionary.append(word)

while True:
    query = input()
    if query == "#":
        break

    if query in dictionary:
        print(f"{query} is correct")
    else:
        similar_words = []
        for word in dictionary:
            if is_similar(query, word):
                similar_words.append(word)
        print(f"{query}: {' '.join(similar_words)}")