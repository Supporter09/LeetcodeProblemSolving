# Idea
# Iterate through each element
# Check if target - x exist 
# If exist: return index of target and target - x
# If not: diction[x] = index_x

# TC: O(n)
# SC: O(n)

def twoSum(nums, target):
    diction = {}

    for i in range(len(nums)):
        if diction.get(target - nums[i]) != None:
            res = [i, diction[target - nums[i]]]
            return res
        else:
            diction[nums[i]] = i

print(twoSum([3, 3], 6))