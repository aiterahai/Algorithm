E, S, M = map(int, input().split())
count = 1
i, j, k = 1, 1, 1
while not(i == E and j == S and k == M):
    i = (i % 15) + 1
    j = (j % 28) + 1
    k = (k % 19) + 1
    count += 1
print(count)