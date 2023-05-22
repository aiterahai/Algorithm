from sys import stdin
from collections import deque


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    house = list(map(int, stdin.readline().split()))
    store = [list(map(int, stdin.readline().split())) for _ in range(N)]
    rock = list(map(int, stdin.readline().split()))
    visit = [False for _ in range(N)]

    Q = deque([house])
    result = "sad"
    while Q:
        x, y = Q.popleft()
        if manhattan(*rock, x, y) <= 1000:
            result = "happy"
            break
        for idx, value in enumerate(store):
            if visit[idx]: continue
            nx, ny = value
            if manhattan(x, y, nx, ny) <= 1000:
                Q.append([nx, ny])
                visit[idx] = True

    print(result)
