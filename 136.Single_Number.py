def singleNumber(nums):
    # Using bitwise operator
    # With XOR: 
    # if XOR same numbers -> it will return 0 
    # if 0 ^ a ( a != 0 ) = a
    a = 0
    for i in nums:
        a = a ^ i
    return a


print(singleNumber([4,1,2,1,2]))