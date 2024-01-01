def findContentChildren( g , s ):
    g.sort()
    s.sort()
    res = 0
    i = 0
    j = 0
    while j < len(s) and i < len(g):
        if s[j] >= g[i]: 
            res += 1
            i += 1
            j += 1
        elif s[i] < g[i]:
            j += 1

    return res

print(findContentChildren([10,9,8,7], [5,6,7,8]))