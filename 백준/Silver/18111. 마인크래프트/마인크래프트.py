from sys import stdin
n, m, b = map(int, stdin.readline().split())
ground = [list(map(int, stdin.readline().split())) for i in range(n)]
min_time, max_height, min_ground, max_ground, columns, rows= 123456789, 123456789, min(map(min, ground)), max(map(max, ground))+1, len(ground), len(ground[0])
for i in range(min_ground, max_ground):
    block = 0
    count = 0
    for j in range(columns):
        for k in range(rows):
            temp = ground[j][k] - i
            if ground[j][k] < i: count += temp * -1
            else: count += temp * 2
            block -= temp
    if(block <= b):
        if (count <= min_time):
            min_time = count
            max_height = i
print(min_time, max_height)