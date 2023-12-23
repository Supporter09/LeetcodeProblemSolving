def largestPerimeter(nums):
    tmp = sorted(nums)
    # print(tmp)
    prefix_sum = [0]*len(tmp)
    prefix_sum[0] = tmp[0]
    for i in range(1, len(tmp)):
        prefix_sum[i] = tmp[i] + prefix_sum[i-1]
    # print(prefix_sum)
    index = len(tmp)
    for j in range(len(tmp)-1,-1, -1):
        if prefix_sum[j-1] <= tmp[j]:
            index = j
        else:
            break
    res_arr = tmp[:index]
    if len(res_arr) >= 3:
        return sum(res_arr)
    else: return -1
   

print(largestPerimeter([5,5,5]))