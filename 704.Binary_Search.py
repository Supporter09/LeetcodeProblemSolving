# Idea of binary search:
# With a sorted array: nums = [-1,0,3,5,9,12], target = 9
# if mid = l + (r-l) // 2 is:
# = target : return the index
# > target: r = mid - 1 (because the target is at the lower side)
# < target: l = mid + 1 (because the target is at the higher side) 

def search(nums, target):
    # Define two pointer 
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2 # Use this to prevent overflow if the len(nums) is too big
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1

print(search([-1,0,3,5,9,12], 3))

