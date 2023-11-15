def generateParenthesis(n):
    # only add open parentheses if open < n
    # only add closing parentheses if closed < open
    # valid res if open == closed == n
    
    stack = []
    res = []

    def backtracking(openP, closedP):
        if openP == closedP == n:
            res.append("".join(stack))
            return
        
        if openP < n:
            stack.append("(")
            backtracking(openP + 1, closedP)
            stack.pop()
        
        if closedP < openP:
            stack.append(")")
            backtracking(openP, closedP + 1)
            stack.pop()

    backtracking(0, 0)
    print(res)
    return res

generateParenthesis(3)