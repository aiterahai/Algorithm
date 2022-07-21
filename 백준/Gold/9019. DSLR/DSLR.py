from collections import deque
from sys import stdin

for _ in range(int(stdin.readline())):
    visit = [False for i in range(10000)]
    A, B = map(int, stdin.readline().split())
    Q = deque([[A, ""]])
    visit[A] = True
    while Q:
        value, cmd = Q.popleft()
        if value == B:
            print(cmd)
            break
        for i, j in [[((value%10)*1000+value//10)%10000, "R"], [((value%1000)*10+value//1000)%10000, "L"], [(value*2)%10000, "D"], [(value-1)%10000, "S"]]:
            if visit[i]: continue
            visit[i] = True
            Q.append([i, cmd + j])