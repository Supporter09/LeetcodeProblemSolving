# First idea
# check s == s[::-1]

# Second idea
# The same with first idea but write down by two pointer approach

def isPalindrome(s):
    # Process string
    arr = [x.lower() for x in s if x.isalnum()]
    s = ''.join(arr)

    i = 0
    j = len(s) - 1

    while i <= j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

print(isPalindrome(" "))