temp = input()
while temp != '.':
    stack = []
    for i in temp:
        if i == "(" or i == "[" or i == ")" or i == "]":
            stack.append(i)
        if len(stack) >= 2:
            if(stack[-2] == "(" and stack[-1] == ")"):
                stack.pop()
                stack.pop()
            elif (stack[-2] == "[" and stack[-1] == "]"):
                stack.pop()
                stack.pop()
    if(len(stack) == 0):
        print("yes")
    else:
        print("no")
    temp = input()