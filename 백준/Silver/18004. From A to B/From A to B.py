N, M = map(int, input().split())
count = 0
while N != M:
    if N < M:
        count += M - N
        break
    else:
        if N % 2: N, count = N + 1, count + 1
        else: N, count = N // 2, count + 1
print(count)