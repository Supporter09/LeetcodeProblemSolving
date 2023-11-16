# Sliding Window
def lengthOfLongestSubstring(s):
    arr = []
    res = 0

    for index in range(len(s)):
        if s[index] not in arr:
            arr.append(s[index])
        else:
            if len(arr) > res: res = len(arr)
            while arr and s[index] in arr:
                arr.pop(0)
            arr.append(s[index])
    if len(arr) > res: return len(arr)
    return res

print(lengthOfLongestSubstring(" "))