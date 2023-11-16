def findDifferentBinaryString(nums):
    res = ''
    for i, num in enumerate(nums):
        if num[i] == '0':
            res += '1'
        elif num[i] == '1':
            res += '0'
    print(res)
    return res
findDifferentBinaryString(["01","10"])