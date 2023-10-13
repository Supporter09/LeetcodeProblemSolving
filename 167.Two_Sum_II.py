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