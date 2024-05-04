def lengthOfLastWord(s):
    return len(s.strip().split()[-1])


print(lengthOfLastWord("Hello World    ball   "))
