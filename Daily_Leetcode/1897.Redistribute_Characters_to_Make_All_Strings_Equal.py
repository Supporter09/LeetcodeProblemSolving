def makeEqual(words):
    check_dict = dict()
    if len(words) == 1:
        return True

    for word in words:
        for char in word:
            check_dict[char] = check_dict.get(char, 0) + 1

    for key in check_dict:
        if check_dict[key] % len(words) != 0:
            return False

    return True

print(makeEqual(["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"]))