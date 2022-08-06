from sys import stdin

board = stdin.readline().rstrip()
if len(board) == 1: print(0); exit(0)
stack = []
for i in board:
    stack.append(i)
    if len(stack) >= 2 and stack[-2] == "(" and stack[-1] == ")":
        stack.pop()
        stack.pop()
        stack.append("2")
    if len(stack) >= 2 and stack[-2] == "[" and stack[-1] == "]":
        stack.pop()
        stack.pop()
        stack.append("3")
    if len(stack) >= 3 and stack[-3] == "(" and stack[-2].isdigit() and stack[-1] == ")":
        stack.pop()
        temp = stack.pop()
        stack.pop()
        stack.append(str(int(temp) * 2))
    if len(stack) >= 3 and stack[-3] == "[" and stack[-2].isdigit() and stack[-1] == "]":
        stack.pop()
        temp = stack.pop()
        stack.pop()
        stack.append(str(int(temp) * 3))
    if len(stack) >= 2 and stack[-1].isdigit() and stack[-2].isdigit():
        stack.append(str(int(stack.pop()) + int(stack.pop())))
print(stack[0] if len(stack) == 1 else 0)