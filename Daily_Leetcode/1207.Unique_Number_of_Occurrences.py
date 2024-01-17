from collections import Counter
def uniqueOccurrences(arr):
    freq = Counter(arr)
    values = list(freq.values())
    check = set(values)
    return len(check) == len(list(values))

print(uniqueOccurrences([1,2,2,1,1,3]))