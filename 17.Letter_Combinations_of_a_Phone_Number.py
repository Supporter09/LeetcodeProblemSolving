def letterCombinations(digits):
    if not digits: # No digit => Empty result
        return []
    
    # Initialize a map between number and characters
    char_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    result = []
    comb = []

    def backtrack(i):
        if i >= len(digits) :
            result.append(''.join(comb))
            return 
        
        for char in char_map[digits[i]]: # Try every possible characters
            comb.append(char)
            backtrack(i+1)
            comb.pop()

    backtrack(0)
    return result

print(letterCombinations(""))
