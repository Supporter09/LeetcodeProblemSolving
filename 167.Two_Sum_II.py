# Input
# [2, 3, 4, 7, 11] target = 9

# Two-pointer
# l = 0 ; r = len(nums) -1

# nums[l] + nums[r] :
# TH1: sum = target => return 
# TH2: sum > target: r -= 1
# TH3: sum < target: l += 1

def twoSum(numbers, target):
    # Set Up Two Pointer
    l = 0
    r = len(numbers) - 1

    # Traversal with two pointer
    while l <= r:
        if numbers[l] + numbers[r] == target: 
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1
    
print(twoSum([-1,0], -1))