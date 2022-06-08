n = int(input())
towers = list(map(int, input().split()))
stack = []
result = []

for i in range(n):
    while len(stack) != 0:
        if stack[-1][1] > towers[i]:
            result.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if len(stack) == 0:
        result.append(0)
    stack.append([i, towers[i]])

print(" ".join(map(str, result)))