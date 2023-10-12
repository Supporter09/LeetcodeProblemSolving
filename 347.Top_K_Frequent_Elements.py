# Idea: bind the frequency of each unique number to an dictionary
# Sort the keys, values according to each element frequency
# TC: O(n.log(n))

def topKFrequent(nums, k):
    diction = {}

    for num in nums:
        diction[num] = diction.get(num, 0) + 1

    res = []

    items = list(diction.items())
    items.sort(key = lambda x: x[1], reverse= True)

    res = []
    
    for i in range(k):
        res.append(items[i][0])

    return res

print(topKFrequent([3,0,1,0], 1))
