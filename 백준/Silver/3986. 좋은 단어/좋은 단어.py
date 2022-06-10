from sys import stdin
n = int(stdin.readline())
count = 0
for i in range(n):
    stack = []
    stack_len = 0
    temp = stdin.readline()[:-1]
    if(len(temp) % 2 == 0):
        for j in temp:
            stack.append(j)
            stack_len += 1
            while(stack_len >= 2 and stack[-1] == stack[-2]):
                stack.pop()
                stack.pop()
                stack_len -= 2
        if stack_len == 0: count += 1
print(count)