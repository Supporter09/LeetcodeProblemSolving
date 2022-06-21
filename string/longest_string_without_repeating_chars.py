userInput = open('D:\Code\Leetcode\string\LOLS.IN.txt','r')
def lengthOfLongestSubstring(string):
	longest_str = ""
	for i in range(len(string)):
		tmp_str = "" + string[i]
		for j in range(i+1,len(string)):
			if string[j] not in tmp_str:
				tmp_str += string[j]
			else: 
				break
		if len(tmp_str) > len(longest_str):
			longest_str = tmp_str
	return longest_str
output = open('D:\Code\Leetcode\string\LOLS.OUT.txt','w')
test_cases = int(userInput.readline())
for i in range(test_cases):
	user_string = userInput.readline().replace('\n','')
	result = lengthOfLongestSubstring(user_string)
	message = "Test case lan " + str(i) 
	output.write(message + "\n")
	output.write(result + "\n")
	output.write(str(len(result)) + "\n")

