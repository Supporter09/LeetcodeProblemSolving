# Idea - Using stack data structure
# - If it is an opened bracket: add to stack
# - If it is an closed bracket: check the nearest bracket
# if the bracket match
# How to check if it is closed bracket and matched => Using Hash map
# closeOpenBracket = {')': '(', ']': '[', '}': '{' }

# Ex: '[({})]'
# '[' -> add (stack: ['['])
# '(' -> add (stack: ['[', '(' ])
# '{' -> add (stack: ['[', '(', '{' ])
# '}' -> check last el of stack ('{') => matched => pop '{'
# ')' -> check last el of stack ('(') => matched => pop '('
# ']' -> check last el of stack ('[') => matched => pop '['

# Done => stack [] => return True

def isValid(s):
    # Create stack
    stack = []

    # Create hashmap
    closeOpenBracket = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in closeOpenBracket:
            if stack and stack[-1] == closeOpenBracket[char]:
                stack.pop()
            else: # Don't match => not valid. Ex: '(})'
                return False
        else: # Opened bracket => Add to stack
            stack.append(char)

    return True if not stack else False

print(isValid("()[]{}"))