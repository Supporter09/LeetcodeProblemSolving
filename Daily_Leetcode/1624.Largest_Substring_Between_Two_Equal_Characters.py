def maxLengthBetweenEqualCharacters(s):
    char_ord = dict()
    max_len = -1
    for i in range(len(s)):
        if s[i] not in char_ord:
            char_ord[s[i]] = [i + 1, -1]
        else:
            char_ord[s[i]][1] = i + 1 if i + 1 > char_ord[s[i]][1] else char_ord[s[i]][1]
            max_len = max(max_len, char_ord[s[i]][1] - char_ord[s[i]][0] - 1)
    return max_len

print(maxLengthBetweenEqualCharacters('cbzxy'))