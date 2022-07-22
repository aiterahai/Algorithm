N, M = map(int, input().split())
A = list(map(int, input().split()))[::-1]
B = list(map(int, input().split()))[::-1]
result = []
while A or B:
    if not A: result.append(B.pop())
    elif not B: result.append(A.pop())
    else: result.append(A.pop() if A[-1] < B[-1] else B.pop())
print(*result)