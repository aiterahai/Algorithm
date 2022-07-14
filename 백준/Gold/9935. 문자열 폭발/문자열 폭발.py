command = input()
bomb = input()
stack = []
for i in command:
    stack.append(i)
    if len(stack) < len(bomb): continue
    if "".join(stack[-1*len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()
if stack: print("".join(stack))
else: print("FRULA")