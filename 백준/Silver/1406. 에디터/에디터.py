from sys import stdin

l_stack = list(stdin.readline().rstrip())
r_stack = []
for i in range(int(stdin.readline())):
    command = list(stdin.readline().split())
    if command[0] == "L" and l_stack: r_stack.append(l_stack.pop())
    elif command[0] == "D" and r_stack: l_stack.append(r_stack.pop())
    elif command[0] == "B" and l_stack: l_stack.pop()
    elif command[0] == "P": l_stack.append(command[1])
l_stack.extend(reversed(r_stack))
print("".join(map(str, l_stack)))