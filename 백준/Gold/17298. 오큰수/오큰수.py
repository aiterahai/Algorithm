from sys import stdin

N = int(stdin.readline())
S = list(map(int, stdin.readline().split()))
stack, result = [], []
for i in range(N-1, -1, -1):
    while stack:
        if S[i] < stack[-1]:
            result.append(stack[-1])
            stack.append(S[i])
            break
        else: stack.pop()
    if len(stack) == 0:
        result.append(-1)
        stack.append(S[i])
print(" ".join(map(str, result[::-1])))