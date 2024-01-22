def findErrorNums( nums ):
    nums = sorted(nums)
    check = list(range(1, len(nums)+1))
    visited = {}
    res = []

    for i in range(len(nums)):
        if nums[i] in check: 
            check.remove(nums[i])
        visited[nums[i]] = visited.get(nums[i], 0) + 1
        if visited[nums[i]] == 2:
            res.append(nums[i])

    res.append(check[-1])

    return res

print(findErrorNums([3,2,3,4,6,5]))