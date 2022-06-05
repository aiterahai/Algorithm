n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]
result = [[0 for col in range(m)] for row in range(n)]
q = 0
for i, j in zip(arr, arr2):
    p = 0
    for k, l in zip(i, j):
        result[q][p] = k+l
        p += 1
    q += 1
for i in result:
    for j in i:
        print(j, end=" ")
    print()