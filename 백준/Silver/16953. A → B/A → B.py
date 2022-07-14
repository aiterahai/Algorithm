A, B = map(int, input().split())
count = 1
while True:
    if A == B: break
    if not B % 2: B, count = B // 2, count + 1
    elif B % 10 == 1: B, count = B // 10, count + 1
    else:
        print(-1)
        exit(0)
    if B == 0:
        print(-1)
        exit(0)
print(count)