from sys import stdin
n = int(stdin.readline())
buildings = [int(stdin.readline()) for i in range(n)]
stack = []
count = 0
for i in range(n):
    while stack and stack[-1] <= buildings[i]: stack.pop()
    stack.append(buildings[i])
    count += len(stack)-1
print(count)