# Idea: 
# Stack:
# If number => add to stack
# If operations => pop 2 previous number and calculus with that operation and add to stacks
# Then repeat
def evalRPN(tokens):
    # Define stack to use
    stack = []

    for element in tokens:
        if element == '+':
            stack.append(stack.pop() + stack.pop())
        elif element == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif element == '*':
            stack.append(stack.pop() * stack.pop())
        elif element == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else: 
            stack.append(int(element))
            
    print(stack[0])
    return stack[0]

evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])

