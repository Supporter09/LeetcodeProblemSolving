userInput = open('D:\Code\Leetcode\string\FMSA.IN.txt','r')
def findMedianSortedArrays(arr1,arr2):
    a=len(nums1)+len(nums2)
    for i in range(len(nums2)):
        nums1.append(nums2[i])
    nums1.sort()
    if(a%2!=0):
        return nums1[a//2]
    else:
        return (nums1[a//2-1]+nums1[a//2])/2

	

output = open('D:\Code\Leetcode\string\FMSA.OUT.txt','w')
test_cases = int(userInput.readline())
for i in range(test_cases):
    nums1 = userInput.readline().replace('\n','')
    nums1 = list(map(int, nums1.split(' ')))
    nums2 = userInput.readline().replace('\n','')
    nums2 = list(map(int, nums2.split(' ')))
    result = findMedianSortedArrays(nums1, nums2)
    message = "Test case lan " + str(i) 
    output.write(message + "\n")
    output.write(str(result))
    output.write('\n')