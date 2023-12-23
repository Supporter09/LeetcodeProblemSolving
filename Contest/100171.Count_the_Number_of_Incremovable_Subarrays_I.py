
def incremovableSubarrayCount(nums):
    n = len(nums)
    result = 0

    for i in range(n):
        for j in range(i, n):
            # subarray = nums[i:j+1]
            remain_arr = nums[:i] + nums[j+1:]
            # sorted_remain_arr = sorted(remain_arr)
            freq = {}
            check = True
            if len(remain_arr) > 1:
                freq[remain_arr[0]] = 1
                for k in range(1, len(remain_arr)):
                    freq[remain_arr[k]] = freq.get(remain_arr[k], 0) + 1
                    if freq.get(remain_arr[k], 0) > 1:
                        check = False
                        break 
                    if remain_arr[k-1] >= remain_arr[k]:
                        check = False
                        break
                
            if check: result += 1
    return result

print(incremovableSubarrayCount([8,7,6,6]))