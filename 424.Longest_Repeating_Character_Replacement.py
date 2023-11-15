# Sliding Window
# Idea of unfixed size window
# => We expand the window until it isn't a valid window anymore ((length of the substring) - (the "count of most popular character") = k)
# => We have the best res as possible at that point 
# Therefore, we will slide the window to the right 
# end + 1 => Update if count of new char > max_count => we can continue expand our window => Repeat the process

def characterReplacement(s, k):
    window = []
    count_dict = dict()
    max_count = 0
    res = 0
    for i in range(len(s)):

        window.append(s[i])
        count_dict[s[i]] = count_dict.get(s[i], 0) + 1
        max_count = max(count_dict[s[i]], max_count)

        if len(window) - max_count <= k: # Expanding window
            if len(window) > res: res = len(window)

        else: #Sliding window as current window reach limit
            a = window.pop(0)
            count_dict[a] -= 1

    return res

print(characterReplacement("ABAB",2))
