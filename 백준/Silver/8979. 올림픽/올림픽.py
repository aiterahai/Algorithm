from sys import stdin

N, K = map(int, stdin.readline().split())
country = sorted([list(map(int, stdin.readline().split())) for _ in range(N)], key=lambda x: (x[1], x[2], x[3]), reverse=True)
find = [value[1:] for value in country if value[0] == K][0]

count = 1
for value in country:
    if value[1:] == find:
        print(count)
        break
    count += 1