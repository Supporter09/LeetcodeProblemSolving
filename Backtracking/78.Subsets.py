def subsets(nums):
    res = []

    sub_set = []
    # Using DFS Backtracking
    def dfs(i): # The index of element in list
        # Base case
        if i >= len(nums): #This mean we are below last leaf
            res.append(sub_set.copy()) # This is because list is a mutable object and will be modified
            return
        
        # First option (Add to sub set)
        sub_set.append(nums[i])
        dfs(i + 1)

        # Second option (Don't add to sub set)
        sub_set.pop()
        dfs(i + 1)

    dfs(0)
    print(res)
    return res

subsets([1,2,3])

# DONE 😎😎