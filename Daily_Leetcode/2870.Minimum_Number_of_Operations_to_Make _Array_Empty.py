
def minOperations(nums) -> int:
    # Note: For any n >= 3 can always be written by 2x + 3y
    # Therefore, if freq of any val = 1 => return -1
    unique_vals = set(nums)
    res = 0
    
    for val in unique_vals:
        check = nums.count(val)
        if check == 1: 
            return -1
        
        y = check // 3

        if check - 3*y == 2:
            x = 1
        elif check - 3*y == 1:
            if y > 1: y -= 1
            else: y = 0
            
        x = (check - 3 * y) // 2
        res += (x + y)

    return res

print(minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]))