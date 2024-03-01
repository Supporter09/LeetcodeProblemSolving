from collections import Counter


def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    count = sorted(count.items(), key=lambda x: x[1])

    for i in range(len(count)):
        if k >= count[i][1]:
            k -= count[i][1]
        else:
            return len(count) - i


print(findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3))
