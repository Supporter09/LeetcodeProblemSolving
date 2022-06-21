import string

userInput = open('D:\Code\Leetcode\string\LP.IN.txt','r')
def longestPalindrome(s):
    res = ""
    resLen = 0
    
    for i in range(len(s)):
        
        #odd length
        l, r = i, i
        
        while (l >= 0) and (r < len(s)) and s[l]==s[r]:
            if r-l+1 > resLen:
                resLen = r-l+1
                res = s[l:r+1]
            l -= 1
            r += 1
        
        # even length
        l,r = i, i+1
        while (l >= 0) and (r < len(s)) and s[l]==s[r]:
            if r-l+1 > resLen:
                resLen = r-l+1
                res = s[l:r+1]
            l -= 1
            r += 1
            
    return res

output = open('D:\Code\Leetcode\string\LP.OUT.txt','w')
test_cases = int(userInput.readline())
for i in range(test_cases):
	user_string = userInput.readline().replace('\n','')
	result = longestPalindrome(user_string)
	message = "Test case lan " + str(i) 
	output.write(message + "\n")
	output.write(result + "\n")

