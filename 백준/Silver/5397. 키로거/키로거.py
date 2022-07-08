from sys import stdin

T = int(stdin.readline())
for i in range(T):
    command = stdin.readline()[:-1]
    l_stack = []
    r_stack = []
    for j in command:
        if j == "<":
            if l_stack: r_stack.append(l_stack.pop())
        elif j == ">":
            if r_stack: l_stack.append(r_stack.pop())
        elif j == "-":
            if l_stack: l_stack.pop()
        else: l_stack.append(j)
    print("".join((l_stack + r_stack[::-1])))