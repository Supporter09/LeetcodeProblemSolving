def findMatrix(nums):
    res = [[]]
     
    for num in nums:
        i = 0
        check = False
        while i < len(res):
            if num not in res[i]:
                res[i] = res[i] + [num]
                check = True
                break
            i += 1
        if not check:
            res.append([num])
    
    return res

print(findMatrix([1,2,3,4]))