def longestIdealString(s, k):
    arr = [x for x in s]
    arr.sort()
    order = [ord(x) for x in arr]
    print(arr)
    print(order)


longestIdealString("acfgbd", 2)
